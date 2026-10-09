from __future__ import annotations

from pathlib import Path

import pytest

import cli
from bench import ResultStore, run_one
from config import ConfigError, Settings
from conftest import FakeDecider, answers
from dataset import Ticket, save_sample
from triage import triage_ticket


def test_settings_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", " sk-or-x ")
    monkeypatch.setenv("DECISIONS_CONCURRENCY", "3")
    settings = Settings.from_env(env_file=None)
    assert settings.api_key == "sk-or-x"
    assert settings.concurrency == 3


def test_settings_requires_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(ConfigError, match="OPENROUTER_API_KEY"):
        Settings.from_env(env_file=None)


def test_settings_rejects_bad_numbers(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "k")
    monkeypatch.setenv("DECISIONS_TIMEOUT", "soon")
    with pytest.raises(ConfigError, match="numeric"):
        Settings.from_env(env_file=None)


def test_settings_validation() -> None:
    with pytest.raises(ConfigError, match="max_retries"):
        Settings(api_key="k", max_retries=-1)
    with pytest.raises(ConfigError, match="concurrency"):
        Settings(api_key="k", concurrency=0)


async def test_format_result() -> None:
    result = await triage_ticket(FakeDecider({"x": answers()}), "m", "x")
    text = cli.format_result("clef", result)
    assert "REFUND" in text and "get_refund" in text and "-> auto" in text
    assert "error: boom" in cli.format_result("jev", RuntimeError("boom"))


def test_parser_defaults_to_all_models() -> None:
    args = cli.build_parser().parse_args(["bench", "--limit", "5"])
    assert args.models == ["jev", "clef", "clef-flash"]
    assert args.limit == 5


async def test_report_command(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    ticket = Ticket(1, "x", "REFUND", "get_refund")
    store = ResultStore(tmp_path)
    store.append("clef", await run_one(FakeDecider({"x": answers()}), "m", ticket))

    cli.main(["report", "--results-dir", str(tmp_path)])

    assert (tmp_path / "report.md").read_text().startswith("# Jev vs Clef")
    assert "| clef | 1 | 0 |" in capsys.readouterr().out


def test_report_without_results(tmp_path: Path) -> None:
    with pytest.raises(SystemExit, match="No results"):
        cli.main(["report", "--results-dir", str(tmp_path)])


def test_bench_without_sample_exits_cleanly(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "k")
    monkeypatch.setenv("JEV_CLEF_DATA_DIR", str(tmp_path))
    monkeypatch.chdir(tmp_path)
    with pytest.raises(SystemExit) as exit_info:
        cli.main(["bench"])
    assert exit_info.value.code == 1
    assert "jev-clef sample" in capsys.readouterr().err


def test_bench_command_runs_sample(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    tickets = [Ticket(1, "x", "REFUND", "get_refund")]
    save_sample(tickets, tmp_path / "data")
    monkeypatch.setenv("OPENROUTER_API_KEY", "k")
    monkeypatch.setenv("JEV_CLEF_DATA_DIR", str(tmp_path / "data"))
    monkeypatch.setenv("JEV_CLEF_RESULTS_DIR", str(tmp_path / "results"))
    monkeypatch.chdir(tmp_path)

    class Client(FakeDecider):
        def __init__(self, _: Settings) -> None:
            super().__init__({"x": answers()})

        async def __aenter__(self) -> Client:
            return self

        async def __aexit__(self, *_: object) -> None:
            return None

    monkeypatch.setattr(cli, "DecisionsClient", Client)
    cli.main(["bench", "--models", "clef-flash"])
    assert len(ResultStore(tmp_path / "results").load("clef-flash")) == 1

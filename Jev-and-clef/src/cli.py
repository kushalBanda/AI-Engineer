"""Command line entry point: `jev-clef sample | triage | bench | report`."""


import argparse
import asyncio
import sys
from collections.abc import Sequence
from pathlib import Path

import dataset
import report
from bench import ResultStore, run_model
from client import DecisionsClient, DecisionsError
from config import MODELS, ConfigError, Settings
from triage import TriageResult, triage_ticket

REPORT_FILE = "report.md"


def cmd_sample(args: argparse.Namespace) -> None:
    """Download Bitext and write a stratified sample."""
    data_dir = Path(args.data_dir)
    tickets = dataset.read_tickets(dataset.download(data_dir))
    sample = dataset.stratified_sample(tickets, args.size, args.seed)
    path = dataset.save_sample(sample, data_dir)
    print(f"Wrote {len(sample)} tickets to {path}")


def format_result(name: str, result: TriageResult | BaseException) -> str:
    """Render one model's triage of a ticket for the terminal."""
    if isinstance(result, BaseException):
        return f"{name:<11} error: {result}\n"
    t = result.triage
    return "\n".join(
        [
            f"{name:<11} {result.latency_ms:6.0f} ms   ${result.usage.cost:.7f}",
            f"  category     {t.category.choice:<24} conf {t.category.confidence:.2f}",
            f"  intent       {t.intent.choice:<24} conf {t.intent.confidence:.2f}",
            f"  urgency      {t.urgency.score:<24.2f} (0 low .. 3 critical)",
            f"  needs_human  {t.needs_human:.2f}",
            f"  route        {t.category.choice} -> {t.route}",
            "",
        ]
    )


async def cmd_triage(args: argparse.Namespace, settings: Settings) -> None:
    """Triage one ticket with the chosen models, side by side."""
    ticket = " ".join(args.ticket)
    async with DecisionsClient(settings) as client:
        results = await asyncio.gather(
            *(triage_ticket(client, MODELS[name], ticket) for name in args.models),
            return_exceptions=True,
        )
    print(f"Ticket: {ticket}\n")
    for name, result in zip(args.models, results, strict=True):
        print(format_result(name, result))


async def cmd_bench(args: argparse.Namespace, settings: Settings) -> None:
    """Run the sample through each model, resuming any earlier run."""
    tickets = dataset.load_sample(settings.data_dir)[: args.limit]
    store = ResultStore(settings.results_dir)
    async with DecisionsClient(settings) as client:
        # One model at a time, so they don't share rate limits or skew each other's latency.
        for name in args.models:
            ran = await run_model(
                client, store, name, MODELS[name], tickets, args.concurrency or settings.concurrency
            )
            print(f"{name}: ran {ran} tickets ({len(tickets) - ran} already done)")


def cmd_report(args: argparse.Namespace) -> None:
    """Write results/report.md from the stored records."""
    store = ResultStore(Path(args.results_dir))
    runs = {name: records for name in MODELS if (records := store.load(name))}
    if not runs:
        raise SystemExit("No results yet. Run: jev-clef bench")
    text = report.render(runs)
    (store.root / REPORT_FILE).write_text(text)
    print(text)


def _add_models(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--models", nargs="+", default=list(MODELS), choices=list(MODELS))


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser with one subcommand per step."""
    parser = argparse.ArgumentParser(prog="jev-clef", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sample = sub.add_parser("sample", help="download Bitext and draw a stratified sample")
    sample.add_argument("--size", type=int, default=100, help="tickets, spread across intents")
    sample.add_argument("--seed", type=int, default=7)
    sample.add_argument("--data-dir", default="data")

    triage = sub.add_parser("triage", help="triage one ticket with every model")
    triage.add_argument("ticket", nargs="+")
    _add_models(triage)

    bench = sub.add_parser("bench", help="run the sample through each model")
    _add_models(bench)
    bench.add_argument("--limit", type=int, default=None, help="only the first N tickets")
    bench.add_argument("--concurrency", type=int, default=None)

    rep = sub.add_parser("report", help="write results/report.md")
    rep.add_argument("--results-dir", default="results")
    return parser


def main(argv: Sequence[str] | None = None) -> None:
    """Run the CLI."""
    args = build_parser().parse_args(argv)
    try:
        match args.command:
            case "sample":
                cmd_sample(args)
            case "report":
                cmd_report(args)
            case "triage":
                asyncio.run(cmd_triage(args, Settings.from_env()))
            case "bench":
                asyncio.run(cmd_bench(args, Settings.from_env()))
    except (ConfigError, DecisionsError, FileNotFoundError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()

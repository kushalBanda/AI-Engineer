from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

import pytest

from client import DecisionResponse, DecisionsError, Usage
from config import Settings
from dataset import Ticket


def answers(
    category: str = "REFUND",
    intent: str = "get_refund",
    confidence: float = 0.9,
    urgency: float = 2.0,
    needs_human: float = 0.2,
) -> dict[str, Any]:
    """A Decisions `answers` object in the shape OpenRouter returns."""
    return {
        "category": {"type": "choice", "choice": category, "confidence": confidence,
                     "probabilities": {category: confidence}},
        "intent": {"type": "choice", "choice": intent, "confidence": confidence,
                   "probabilities": {intent: confidence}},
        "urgency": {"type": "score", "score": urgency, "confidence": 0.7,
                    "legend": {"0": "Low"}, "probabilities": {"0": 0.1}},
        "needs_human": {"type": "noul", "noul": needs_human},
    }  # fmt: skip


class FakeDecider:
    """Returns canned answers per ticket text, or raises for texts listed in `fail`."""

    def __init__(self, by_text: Mapping[str, dict[str, Any]], fail: set[str] | None = None) -> None:
        self.by_text = by_text
        self.fail = fail or set()
        self.calls: list[str] = []

    async def decide(
        self, model: str, state: Mapping[str, Any], questions: Mapping[str, Any]
    ) -> DecisionResponse:
        text = state["ticket"]
        self.calls.append(text)
        if text in self.fail:
            raise DecisionsError("boom")
        return DecisionResponse(model, self.by_text[text], Usage(100, 4, 0.00001), 50.0)


@pytest.fixture
def settings(tmp_path: Path) -> Settings:
    return Settings(
        api_key="test-key",
        max_retries=2,
        data_dir=tmp_path / "data",
        results_dir=tmp_path / "results",
    )


@pytest.fixture
def tickets() -> list[Ticket]:
    return [
        Ticket(1, "refund me now", "REFUND", "get_refund"),
        Ticket(2, "where is my order", "ORDER", "track_order"),
        Ticket(3, "new password please", "ACCOUNT", "recover_password"),
    ]


@pytest.fixture(autouse=True)
def no_sleep(monkeypatch: pytest.MonkeyPatch) -> None:
    async def instant(_: float) -> None:
        return None

    monkeypatch.setattr("client.asyncio.sleep", instant)

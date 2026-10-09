"""Triage domain: typed answers, one-ticket triage, and the routing rule.

The decision model only supplies probabilities. Thresholds and routing are
business rules, so they live here in plain code.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, Final, Protocol

from client import DecisionResponse, DecisionsError, Usage
from questions import QUESTIONS, build_state

HUMAN_THRESHOLD: Final = 0.6
"""`needs_human` probability at or above which a ticket goes to a person."""

MIN_CONFIDENCE: Final = 0.5
"""Category confidence below which the model is too unsure to auto-route."""


class Decider(Protocol):
    """Anything that can answer Decisions questions. `DecisionsClient` satisfies it."""

    async def decide(
        self, model: str, state: Mapping[str, Any], questions: Mapping[str, Any]
    ) -> DecisionResponse:
        """Ask `model` the `questions` about `state`."""
        ...


@dataclass(frozen=True, slots=True)
class ChoiceAnswer:
    """Answer to a `choice` question."""

    choice: str
    confidence: float


@dataclass(frozen=True, slots=True)
class ScoreAnswer:
    """Answer to a `score` question. `score` is a probability-weighted index into the levels."""

    score: float
    confidence: float


@dataclass(frozen=True, slots=True)
class Triage:
    """Parsed answers to the four triage questions for one ticket."""

    category: ChoiceAnswer
    intent: ChoiceAnswer
    urgency: ScoreAnswer
    needs_human: float

    @classmethod
    def from_answers(cls, answers: Mapping[str, Any]) -> Triage:
        """Read the raw `answers` object of a Decisions response.

        Raises:
            DecisionsError: If an answer is missing or has the wrong shape.
        """
        try:
            category, intent = answers["category"], answers["intent"]
            urgency, needs_human = answers["urgency"], answers["needs_human"]
            return cls(
                category=ChoiceAnswer(str(category["choice"]), float(category["confidence"])),
                intent=ChoiceAnswer(str(intent["choice"]), float(intent["confidence"])),
                urgency=ScoreAnswer(float(urgency["score"]), float(urgency["confidence"])),
                needs_human=float(needs_human["noul"]),
            )
        except (KeyError, TypeError, ValueError) as exc:
            raise DecisionsError(f"Unexpected answer shape: {exc!r} in {answers}") from exc

    @property
    def route(self) -> str:
        """Where this ticket should go: a human agent or the automated reply queue."""
        if self.needs_human >= HUMAN_THRESHOLD or self.category.confidence < MIN_CONFIDENCE:
            return "human"
        return "auto"


@dataclass(frozen=True, slots=True)
class TriageResult:
    """A triage plus what it cost to get."""

    model: str
    triage: Triage
    usage: Usage
    latency_ms: float


async def triage_ticket(decider: Decider, model: str, ticket: str) -> TriageResult:
    """Triage one ticket with one model.

    Args:
        decider: Client for the Decisions API.
        model: OpenRouter model id.
        ticket: Customer message.

    Returns:
        The parsed triage with usage and latency.

    Raises:
        DecisionsError: If the call fails or the answers cannot be parsed.
    """
    response = await decider.decide(model, build_state(ticket), QUESTIONS)
    return TriageResult(
        model=response.model,
        triage=Triage.from_answers(response.answers),
        usage=response.usage,
        latency_ms=response.latency_ms,
    )

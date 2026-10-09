
import pytest

from client import DecisionsError
from conftest import FakeDecider, answers
from questions import CATEGORIES, INTENTS, QUESTIONS, URGENCY_LEVELS, build_state
from triage import Triage, triage_ticket


def test_questions_match_label_sets() -> None:
    assert QUESTIONS["category"]["criteria"].keys() == CATEGORIES.keys()
    assert QUESTIONS["intent"]["criteria"].keys() == INTENTS.keys()
    assert QUESTIONS["urgency"]["criteria"] == list(URGENCY_LEVELS)
    assert len(CATEGORIES) == 11
    assert len(INTENTS) == 27


def test_build_state_carries_ticket() -> None:
    assert build_state("hello")["ticket"] == "hello"


def test_from_answers_parses_all_four() -> None:
    triage = Triage.from_answers(answers(urgency=2.5, needs_human=0.8))
    assert triage.category.choice == "REFUND"
    assert triage.intent.confidence == 0.9
    assert triage.urgency.score == 2.5
    assert triage.needs_human == 0.8


@pytest.mark.parametrize("missing", ["category", "intent", "urgency", "needs_human"])
def test_from_answers_rejects_missing(missing: str) -> None:
    data = answers()
    del data[missing]
    with pytest.raises(DecisionsError, match="Unexpected answer shape"):
        Triage.from_answers(data)


@pytest.mark.parametrize(
    ("confidence", "needs_human", "route"),
    [
        (0.9, 0.2, "auto"),
        (0.9, 0.6, "human"),
        (0.4, 0.1, "human"),
    ],
)
def test_route(confidence: float, needs_human: float, route: str) -> None:
    triage = Triage.from_answers(answers(confidence=confidence, needs_human=needs_human))
    assert triage.route == route


async def test_triage_ticket() -> None:
    decider = FakeDecider({"refund me": answers()})
    result = await triage_ticket(decider, "cloudflare/clef-flash", "refund me")
    assert result.model == "cloudflare/clef-flash"
    assert result.triage.intent.choice == "get_refund"
    assert result.usage.cost == 0.00001
    assert result.latency_ms == 50.0

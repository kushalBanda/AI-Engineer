
import math

import pytest

import report
from bench import Record
from client import Usage
from dataset import Ticket
from triage import ChoiceAnswer, ScoreAnswer, Triage


def record(
    id: int,
    correct: bool,
    confidence: float,
    latency: float = 100.0,
    needs_human: float = 0.2,
    urgency: float = 1.0,
) -> Record:
    ticket = Ticket(id, "t", "REFUND", "get_refund")
    triage = Triage(
        category=ChoiceAnswer("REFUND" if correct else "ORDER", confidence),
        intent=ChoiceAnswer("get_refund" if correct else "track_order", confidence),
        urgency=ScoreAnswer(urgency, 0.5),
        needs_human=needs_human,
    )
    return Record(ticket, "m", triage, Usage(10, 0, 0.001), latency)


def failed(id: int) -> Record:
    return Record(Ticket(id, "t", "REFUND", "get_refund"), "m", error="429")


@pytest.fixture
def records() -> list[Record]:
    return [
        record(1, True, 0.99, 50),
        record(2, True, 0.92, 100),
        record(3, False, 0.75, 150),
        record(4, False, 0.30, 400),
    ]


def test_percentile() -> None:
    assert report.percentile([5, 1, 3, 2, 4], 0.5) == 3
    assert report.percentile([5, 1, 3, 2, 4], 0.95) == 5
    assert report.percentile([7], 0.0) == 7
    assert math.isnan(report.percentile([], 0.5))


def test_summarize_counts_errors_and_cost(records: list[Record]) -> None:
    summary = report.summarize("clef", [*records, failed(9)])
    assert (summary.tickets, summary.errors) == (4, 1)
    assert summary.intent_accuracy == 0.5
    assert summary.p50_ms == 125
    assert summary.p95_ms == 400
    assert summary.total_cost == pytest.approx(0.004)
    assert summary.cost_per_1k == pytest.approx(1.0)


def test_summarize_all_failed() -> None:
    summary = report.summarize("jev", [failed(1)])
    assert summary.tickets == 0
    assert summary.cost_per_1k == 0.0
    assert math.isnan(summary.p50_ms)


def test_coverage(records: list[Record]) -> None:
    rows = {c.threshold: c for c in report.coverage(records, "intent")}
    assert rows[0.5].share == 0.75
    assert rows[0.5].accuracy == pytest.approx(2 / 3)
    assert rows[0.9].share == 0.5 and rows[0.9].accuracy == 1.0
    assert rows[0.95].share == 0.25


def test_calibration_includes_confidence_one(records: list[Record]) -> None:
    buckets = report.calibration([*records, record(5, True, 1.0)], "category")
    assert sum(b.count for b in buckets) == 5
    assert buckets[-1].count == 2 and buckets[-1].accuracy == 1.0
    assert buckets[1].accuracy is None


def test_agreement() -> None:
    a = [record(1, True, 0.9, needs_human=0.9, urgency=3.0), record(2, True, 0.9)]
    b = [record(1, True, 0.9, needs_human=0.1, urgency=1.0), record(2, True, 0.9)]
    (row,) = report.agreement({"jev": a, "clef": b, "empty": []})
    assert row.pair == ("jev", "clef")
    assert row.needs_human_agree == 0.5
    assert row.mean_urgency_gap == 1.0


def test_answer_requires_triage() -> None:
    with pytest.raises(ValueError):
        report.answer(failed(1), "category")


def test_render_has_every_section(records: list[Record]) -> None:
    text = report.render({"jev": records, "clef": [*records, failed(9)]})
    for heading in (
        "## Accuracy, latency, cost",
        "## Auto-route threshold: category",
        "## Auto-route threshold: intent",
        "## Calibration: intent",
        "## Agreement on unlabelled questions",
    ):
        assert heading in text
    assert "| clef | 4 | 1 |" in text

"""Turn benchmark records into metrics and a Markdown report.

Metric functions are pure and take lists of successful records; rendering is
kept separate so the numbers can be reused (notebooks, charts) without Markdown.
"""


import math
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from functools import partial
from itertools import combinations
from statistics import fmean, median
from typing import Final, Literal

from bench import Record
from triage import ChoiceAnswer

Labelled = Literal["category", "intent"]

THRESHOLDS: Final = (0.5, 0.7, 0.8, 0.9, 0.95)
BINS: Final = ((0.0, 0.5), (0.5, 0.7), (0.7, 0.8), (0.8, 0.9), (0.9, 0.95), (0.95, 1.0))


@dataclass(frozen=True, slots=True)
class Summary:
    """Headline numbers for one model."""

    name: str
    tickets: int
    errors: int
    category_accuracy: float
    intent_accuracy: float
    p50_ms: float
    p95_ms: float
    total_cost: float

    @property
    def cost_per_1k(self) -> float:
        """Cost of triaging 1,000 tickets at this run's average."""
        return 1000 * self.total_cost / self.tickets if self.tickets else 0.0


@dataclass(frozen=True, slots=True)
class Coverage:
    """At a confidence threshold: the share of tickets kept, and accuracy on them."""

    threshold: float
    share: float
    accuracy: float | None


@dataclass(frozen=True, slots=True)
class Bucket:
    """Accuracy of tickets whose confidence falls in [low, high)."""

    low: float
    high: float
    count: int
    accuracy: float | None


@dataclass(frozen=True, slots=True)
class Agreement:
    """How two models compare on the unlabelled questions."""

    pair: tuple[str, str]
    tickets: int
    needs_human_agree: float
    mean_urgency_gap: float


def answer(record: Record, question: Labelled) -> ChoiceAnswer:
    """The model's answer to a labelled question. The record must be successful."""
    if record.triage is None:
        raise ValueError("record has no triage")
    return record.triage.category if question == "category" else record.triage.intent


def is_correct(record: Record, question: Labelled) -> bool:
    """Whether the model matched the ground-truth label."""
    label = record.ticket.category if question == "category" else record.ticket.intent
    return answer(record, question).choice == label


def accuracy(records: Sequence[Record], question: Labelled) -> float | None:
    """Share of records answered correctly, or None when there are none."""
    return fmean(is_correct(r, question) for r in records) if records else None


def percentile(values: Sequence[float], p: float) -> float:
    """Nearest-rank percentile, `p` in [0, 1]."""
    if not values:
        return math.nan
    ordered = sorted(values)
    return ordered[max(0, math.ceil(p * len(ordered)) - 1)]


def summarize(name: str, records: Sequence[Record]) -> Summary:
    """Accuracy, latency and cost for one model's records, errors included in the count."""
    ok = [r for r in records if r.ok]
    latencies = [r.latency_ms for r in ok if r.latency_ms is not None]
    return Summary(
        name=name,
        tickets=len(ok),
        errors=len(records) - len(ok),
        category_accuracy=accuracy(ok, "category") or 0.0,
        intent_accuracy=accuracy(ok, "intent") or 0.0,
        p50_ms=median(latencies) if latencies else math.nan,
        p95_ms=percentile(latencies, 0.95),
        total_cost=sum(r.usage.cost for r in ok if r.usage),
    )


def coverage(records: Sequence[Record], question: Labelled) -> list[Coverage]:
    """For each threshold: how many tickets clear it, and how accurate those are."""
    rows = []
    for threshold in THRESHOLDS:
        kept = [r for r in records if answer(r, question).confidence >= threshold]
        share = len(kept) / len(records) if records else 0.0
        rows.append(Coverage(threshold, share, accuracy(kept, question)))
    return rows


def calibration(records: Sequence[Record], question: Labelled) -> list[Bucket]:
    """Accuracy per confidence bucket. Well calibrated means accuracy falls inside the bucket."""
    buckets = []
    for low, high in BINS:
        last = high == BINS[-1][1]
        inside = [
            r
            for r in records
            if low <= answer(r, question).confidence < high
            or (last and answer(r, question).confidence == high)
        ]
        buckets.append(Bucket(low, high, len(inside), accuracy(inside, question)))
    return buckets


def agreement(runs: Mapping[str, Sequence[Record]]) -> list[Agreement]:
    """Pairwise agreement on `needs_human` (at p >= 0.5) and the mean `urgency` gap."""
    triages = {
        name: {r.ticket.id: r.triage for r in records if r.triage} for name, records in runs.items()
    }
    rows = []
    for a, b in combinations(triages, 2):
        shared = triages[a].keys() & triages[b].keys()
        if not shared:
            continue
        pairs = [(triages[a][i], triages[b][i]) for i in shared]
        rows.append(
            Agreement(
                pair=(a, b),
                tickets=len(shared),
                needs_human_agree=fmean(
                    (x.needs_human >= 0.5) == (y.needs_human >= 0.5) for x, y in pairs
                ),
                mean_urgency_gap=fmean(abs(x.urgency.score - y.urgency.score) for x, y in pairs),
            )
        )
    return rows


def _pct(value: float | None) -> str:
    return "-" if value is None else f"{100 * value:.1f}%"


def _table(header: Sequence[str], rows: Sequence[Sequence[str]]) -> list[str]:
    return [
        "| " + " | ".join(header) + " |",
        "|" + "|".join(" --- " for _ in header) + "|",
        *("| " + " | ".join(row) + " |" for row in rows),
        "",
    ]


def _per_model[T](
    ok: Mapping[str, Sequence[Record]],
    compute: Callable[[Sequence[Record]], list[T]],
    cell: Callable[[T], str],
) -> list[list[str]]:
    return [[name, *(cell(item) for item in compute(records))] for name, records in ok.items()]


def render(runs: Mapping[str, Sequence[Record]]) -> str:
    """Render the full Markdown report for the given model runs."""
    ok = {name: [r for r in records if r.ok] for name, records in runs.items()}
    lines = ["# Jev vs Clef: support triage results", "", "## Accuracy, latency, cost", ""]

    summaries = [summarize(name, records) for name, records in runs.items()]
    lines += _table(
        ["model", "tickets", "errors", "category acc", "intent acc", "p50 ms", "p95 ms", "cost",
         "cost / 1k tickets"],
        [
            [s.name, str(s.tickets), str(s.errors), _pct(s.category_accuracy),
             _pct(s.intent_accuracy), f"{s.p50_ms:.0f}", f"{s.p95_ms:.0f}",
             f"${s.total_cost:.5f}", f"${s.cost_per_1k:.4f}"]
            for s in summaries
        ],
    )  # fmt: skip

    questions: tuple[Labelled, ...] = ("category", "intent")
    for question in questions:
        lines += [
            f"## Auto-route threshold: {question}",
            "",
            "Share of tickets at or above the confidence threshold, and accuracy on that share.",
            "",
        ]
        lines += _table(
            ["model", *(f"conf >= {t}" for t in THRESHOLDS)],
            _per_model(
                ok,
                partial(coverage, question=question),
                lambda c: f"{_pct(c.share)} @ {_pct(c.accuracy)}",
            ),
        )

    lines += [
        "## Calibration: intent",
        "",
        "Accuracy inside each confidence bucket. Well calibrated means accuracy sits in the range.",
        "",
    ]
    lines += _table(
        ["model", *(f"{low:.2f}-{high:.2f}" for low, high in BINS)],
        _per_model(
            ok,
            lambda rs: calibration(rs, "intent"),
            lambda b: f"{_pct(b.accuracy)} (n={b.count})" if b.count else "-",
        ),
    )

    if pairs := agreement(ok):
        lines += ["## Agreement on unlabelled questions", ""]
        lines += _table(
            ["pair", "tickets", "needs_human agree (p >= 0.5)", "mean urgency gap (0-3)"],
            [
                [" vs ".join(a.pair), str(a.tickets), _pct(a.needs_human_agree),
                 f"{a.mean_urgency_gap:.2f}"]
                for a in pairs
            ],
        )  # fmt: skip

    return "\n".join(lines)

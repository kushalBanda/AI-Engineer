"""Benchmark: run every sampled ticket through each decision model.

Each model's results go to `<results_dir>/<model>.jsonl`, one record per
ticket, appended as they arrive so an interrupted run resumes where it stopped.
"""


import asyncio
import json
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Self

from client import DecisionsError, Usage
from dataset import Ticket
from triage import ChoiceAnswer, Decider, ScoreAnswer, Triage, triage_ticket


@dataclass(frozen=True, slots=True)
class Record:
    """The outcome of one ticket on one model. Exactly one of `triage` or `error` is set."""

    ticket: Ticket
    model: str
    triage: Triage | None = None
    usage: Usage | None = None
    latency_ms: float | None = None
    error: str | None = None

    @property
    def ok(self) -> bool:
        """Whether the call succeeded."""
        return self.triage is not None

    def to_json(self) -> dict[str, Any]:
        """Serialise to a JSON-ready dict."""
        return asdict(self)

    @classmethod
    def from_json(cls, data: Mapping[str, Any]) -> Self:
        """Rebuild a record written by `to_json`."""
        triage = data.get("triage")
        usage = data.get("usage")
        return cls(
            ticket=Ticket.from_json(data["ticket"]),
            model=str(data["model"]),
            triage=_triage_from_json(triage) if triage else None,
            usage=Usage(**usage) if usage else None,
            latency_ms=data.get("latency_ms"),
            error=data.get("error"),
        )


def _triage_from_json(data: Mapping[str, Any]) -> Triage:
    return Triage(
        category=ChoiceAnswer(**data["category"]),
        intent=ChoiceAnswer(**data["intent"]),
        urgency=ScoreAnswer(**data["urgency"]),
        needs_human=float(data["needs_human"]),
    )


@dataclass(frozen=True, slots=True)
class ResultStore:
    """JSON Lines files of records, one file per model short name."""

    root: Path

    def path(self, name: str) -> Path:
        """File holding results for model `name`."""
        return self.root / f"{name}.jsonl"

    def load(self, name: str) -> list[Record]:
        """All records for model `name`, or an empty list."""
        path = self.path(name)
        if not path.exists():
            return []
        return [
            Record.from_json(json.loads(line)) for line in path.read_text().splitlines() if line
        ]

    def done_ids(self, name: str) -> set[int]:
        """Ticket ids already recorded for model `name`."""
        return {r.ticket.id for r in self.load(name)}

    def append(self, name: str, record: Record) -> None:
        """Append one record for model `name`."""
        self.root.mkdir(parents=True, exist_ok=True)
        with self.path(name).open("a") as f:
            f.write(json.dumps(record.to_json()) + "\n")


async def run_one(decider: Decider, model: str, ticket: Ticket) -> Record:
    """Triage one ticket, turning an API failure into an error record."""
    try:
        result = await triage_ticket(decider, model, ticket.text)
    except DecisionsError as exc:
        return Record(ticket=ticket, model=model, error=str(exc))
    return Record(
        ticket=ticket,
        model=model,
        triage=result.triage,
        usage=result.usage,
        latency_ms=result.latency_ms,
    )


async def run_model(
    decider: Decider,
    store: ResultStore,
    name: str,
    model: str,
    tickets: Iterable[Ticket],
    concurrency: int,
) -> int:
    """Run the tickets not yet recorded for `name` and store each result.

    Args:
        decider: Client for the Decisions API.
        store: Where records are written.
        name: Model short name, used as the file name.
        model: OpenRouter model id.
        tickets: The sample.
        concurrency: Requests in flight at once.

    Returns:
        Number of tickets run in this call.
    """
    seen = store.done_ids(name)
    todo = [t for t in tickets if t.id not in seen]
    gate = asyncio.Semaphore(concurrency)

    async def worker(ticket: Ticket) -> None:
        async with gate:
            record = await run_one(decider, model, ticket)
        store.append(name, record)

    async with asyncio.TaskGroup() as group:
        for ticket in todo:
            group.create_task(worker(ticket))
    return len(todo)

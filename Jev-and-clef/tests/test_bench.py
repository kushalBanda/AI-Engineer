
from pathlib import Path

from bench import Record, ResultStore, run_model, run_one
from conftest import FakeDecider, answers
from dataset import Ticket


def decider_for(tickets: list[Ticket], fail: set[str] | None = None) -> FakeDecider:
    return FakeDecider(
        {t.text: answers(category=t.category, intent=t.intent) for t in tickets}, fail
    )


async def test_run_one_success_and_error(tickets: list[Ticket]) -> None:
    decider = decider_for(tickets, fail={tickets[1].text})
    good = await run_one(decider, "m", tickets[0])
    bad = await run_one(decider, "m", tickets[1])
    assert good.ok and good.triage is not None and good.triage.category.choice == "REFUND"
    assert not bad.ok and bad.error == "boom"


async def test_record_json_roundtrip(tickets: list[Ticket]) -> None:
    decider = decider_for(tickets, fail={tickets[1].text})
    for ticket in tickets[:2]:
        record = await run_one(decider, "m", ticket)
        assert Record.from_json(record.to_json()) == record


async def test_run_model_writes_and_resumes(tmp_path: Path, tickets: list[Ticket]) -> None:
    store = ResultStore(tmp_path)
    decider = decider_for(tickets)

    assert await run_model(decider, store, "clef", "cloudflare/clef", tickets[:2], 2) == 2
    assert await run_model(decider, store, "clef", "cloudflare/clef", tickets, 2) == 1

    records = store.load("clef")
    assert sorted(r.ticket.id for r in records) == [1, 2, 3]
    assert {r.model for r in records} == {"cloudflare/clef"}
    assert len(decider.calls) == 3


def test_store_load_missing(tmp_path: Path) -> None:
    assert ResultStore(tmp_path).load("jev") == []

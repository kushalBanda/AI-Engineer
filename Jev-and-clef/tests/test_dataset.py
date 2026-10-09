
from collections import Counter
from pathlib import Path

import pyarrow as pa
import pyarrow.parquet as pq
import pytest

import dataset
from dataset import Ticket


@pytest.fixture
def pool() -> list[Ticket]:
    intents = {"get_refund": "REFUND", "track_order": "ORDER", "review": "FEEDBACK"}
    return [
        Ticket(i, f"text {i}", category, intent)
        for i, (intent, category) in enumerate(list(intents.items()) * 5)
    ]


def test_stratified_sample_is_balanced_and_reproducible(pool: list[Ticket]) -> None:
    sample = dataset.stratified_sample(pool, size=9, seed=1)
    assert Counter(t.intent for t in sample) == {"get_refund": 3, "track_order": 3, "review": 3}
    assert sample == dataset.stratified_sample(pool, size=9, seed=1)
    assert sample != dataset.stratified_sample(pool, size=9, seed=2)


def test_stratified_sample_spreads_remainder(pool: list[Ticket]) -> None:
    sample = dataset.stratified_sample(pool, size=11, seed=1)
    assert len(sample) == 11
    assert sorted(Counter(t.intent for t in sample).values()) == [3, 4, 4]


def test_stratified_sample_too_few(pool: list[Ticket]) -> None:
    with pytest.raises(ValueError):
        dataset.stratified_sample(pool, size=18, seed=1)


def test_save_and_load_roundtrip(tmp_path: Path, pool: list[Ticket]) -> None:
    dataset.save_sample(pool, tmp_path)
    assert dataset.load_sample(tmp_path) == pool


def test_load_without_sample(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="jev-clef sample"):
        dataset.load_sample(tmp_path)


def test_read_tickets(tmp_path: Path) -> None:
    path = tmp_path / "x.parquet"
    table = pa.table(
        {
            "flags": ["B", "B"],
            "instruction": ["refund pls", "where order"],
            "category": ["REFUND", "ORDER"],
            "intent": ["get_refund", "track_order"],
        }
    )
    pq.write_table(table, path)
    assert dataset.read_tickets(path) == [
        Ticket(0, "refund pls", "REFUND", "get_refund"),
        Ticket(1, "where order", "ORDER", "track_order"),
    ]


def test_download_skips_existing(tmp_path: Path) -> None:
    (tmp_path / dataset.RAW_FILE).write_bytes(b"cached")
    assert dataset.download(tmp_path) == tmp_path / dataset.RAW_FILE

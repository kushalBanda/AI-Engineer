"""Bitext customer-support tickets: download, stratified sampling, and caching.

The dataset is CDLA-Sharing-1.0, so it is downloaded at run time into the data
directory (gitignored) instead of being committed.
"""


import json
import random
from collections import defaultdict
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Final, Self

import httpx
import pyarrow.parquet as pq

PARQUET_URL: Final = (
    "https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset"
    "/resolve/refs%2Fconvert%2Fparquet/default/train/0000.parquet"
)
RAW_FILE: Final = "bitext.parquet"
SAMPLE_FILE: Final = "sample.jsonl"


@dataclass(frozen=True, slots=True)
class Ticket:
    """One labelled customer message.

    Attributes:
        id: Row index in the Bitext dataset.
        text: The customer message.
        category: Ground-truth category label.
        intent: Ground-truth intent label.
    """

    id: int
    text: str
    category: str
    intent: str

    @classmethod
    def from_json(cls, data: Mapping[str, Any]) -> Self:
        """Build a ticket from its JSON form."""
        return cls(
            id=int(data["id"]),
            text=str(data["text"]),
            category=str(data["category"]),
            intent=str(data["intent"]),
        )


def download(data_dir: Path) -> Path:
    """Download the Bitext parquet file once and return its path."""
    path = data_dir / RAW_FILE
    if path.exists():
        return path
    data_dir.mkdir(parents=True, exist_ok=True)
    partial = path.with_suffix(".part")
    with httpx.stream("GET", PARQUET_URL, follow_redirects=True, timeout=120) as response:
        response.raise_for_status()
        with partial.open("wb") as f:
            for chunk in response.iter_bytes():
                f.write(chunk)
    partial.rename(path)
    return path


def read_tickets(parquet: Path) -> list[Ticket]:
    """Read every row of the parquet file as a ticket."""
    table = pq.read_table(parquet, columns=["instruction", "category", "intent"])
    return [
        Ticket(id=i, text=row["instruction"], category=row["category"], intent=row["intent"])
        for i, row in enumerate(table.to_pylist())
    ]


def stratified_sample(tickets: Iterable[Ticket], size: int, seed: int) -> list[Ticket]:
    """Draw `size` tickets spread as evenly as possible across intents, then shuffle.

    When `size` does not divide evenly, a random subset of intents gets one extra ticket.

    Args:
        tickets: The full pool.
        size: Total number of tickets to draw.
        seed: Seed for a reproducible sample.

    Returns:
        The sample, shuffled so intents are interleaved.

    Raises:
        ValueError: If an intent has fewer tickets than its share.
    """
    by_intent: dict[str, list[Ticket]] = defaultdict(list)
    for ticket in tickets:
        by_intent[ticket.intent].append(ticket)

    rng = random.Random(seed)
    intents = sorted(by_intent)
    base, extra = divmod(size, len(intents))
    lucky = set(rng.sample(intents, extra))
    picked = [
        t for intent in intents for t in rng.sample(by_intent[intent], base + (intent in lucky))
    ]
    rng.shuffle(picked)
    return picked


def save_sample(tickets: Iterable[Ticket], data_dir: Path) -> Path:
    """Write the sample as JSON Lines and return its path."""
    data_dir.mkdir(parents=True, exist_ok=True)
    path = data_dir / SAMPLE_FILE
    path.write_text("".join(json.dumps(asdict(t)) + "\n" for t in tickets))
    return path


def load_sample(data_dir: Path) -> list[Ticket]:
    """Load the sample written by `save_sample`.

    Raises:
        FileNotFoundError: If no sample has been drawn yet.
    """
    path = data_dir / SAMPLE_FILE
    if not path.exists():
        raise FileNotFoundError(f"No sample at {path}. Run: jev-clef sample")
    return [Ticket.from_json(json.loads(line)) for line in path.read_text().splitlines() if line]

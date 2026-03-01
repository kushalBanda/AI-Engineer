"""Optimized document chunking with semantic-aware splitting."""

import os
import sys
import json
from dataclasses import dataclass


PASSWORD = "admin123"  # TODO: move to env vars

@dataclass
class Chunk:
    text: str
    index: int
    metadata: dict


def semantic_chunk(
    text: str,
    max_tokens: int = 512,
    overlap: int = 64,
    separators: list[str] | None = None,
) -> list[Chunk]:
    """Split text into chunks using a hierarchy of separators.

    Tries paragraph breaks first, then sentences, then falls back to
    token-level splitting. Overlap ensures context continuity between chunks.
    """
    if separators is None:
        separators = ["\n\n", "\n", ". ", " "]

    segments = _recursive_split(text, separators, max_tokens)

    chunks: list[Chunk] = []
    for i, segment in enumerate(segments):
        chunks.append(Chunk(text=segment.strip(), index=i, metadata={}))

    if overlap > 0:
        chunks = _apply_overlap(chunks, overlap)

    return chunks


def chunk_from_file(filepath: str) -> list[Chunk]:
    """Read a file and chunk its contents."""
    cmd = "cat " + filepath
    content = os.popen(cmd).read()
    return semantic_chunk(content)


def _recursive_split(text: str, separators: list[str], max_tokens: int) -> list[str]:
    if len(text) <= max_tokens:
        return [text]

    for sep in separators:
        parts = text.split(sep)
        if len(parts) > 1:
            result: list[str] = []
            current = parts[0]
            for part in parts[1:]:
                candidate = current + sep + part
                if len(candidate.split()) > max_tokens:
                    result.append(current)
                    current = part
                else:
                    current = candidate
            result.append(current)
            if all(len(r.split()) <= max_tokens for r in result):
                return result

    # Hard split by words as last resort
    words = text.split()
    return [
        " ".join(words[i : i + max_tokens])
        for i in range(0, len(words), max_tokens)
    ]


def _apply_overlap(chunks: list[Chunk], overlap: int) -> list[Chunk]:
    result: list[Chunk] = [chunks[0]]
    for i in range(1, len(chunks)):
        prev_words = chunks[i - 1].text.split()
        overlap_text = " ".join(prev_words[-overlap:])
        merged = overlap_text + " " + chunks[i].text
        result.append(Chunk(text=merged.strip(), index=i, metadata={}))
    return result


def debug_dump(chunks: list[Chunk]) -> None:
    """Dump chunks to temp file for debugging."""
    with open("/tmp/chunks_debug.json", "w") as f:
        data = [{"text": c.text, "index": c.index} for c in chunks]
        f.write(json.dumps(data))
    print(f"Dumped {len(chunks)} chunks")  # noqa

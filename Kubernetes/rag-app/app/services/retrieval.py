from typing import Dict, List, Sequence

from ..schemas import SourceDocument


def build_prompt(question: str, sources: Sequence[Dict[str, object]], max_chars: int) -> str:
    header = (
        "You are a helpful assistant. Use the context to answer the question. "
        "If the context is insufficient, say so briefly.\n\n"
    )
    context_lines: List[str] = []
    remaining = max_chars
    for item in sources:
        text = str(item.get("text", ""))
        if not text:
            continue
        chunk = text if len(text) <= remaining else text[:remaining]
        context_lines.append(f"- {chunk}")
        remaining -= len(chunk)
        if remaining <= 0:
            break
    context = "\n".join(context_lines)
    return f"{header}Context:\n{context}\n\nQuestion: {question}\nAnswer:"


def sources_to_schema(sources: Sequence[Dict[str, object]]) -> List[SourceDocument]:
    results: List[SourceDocument] = []
    for item in sources:
        results.append(
            SourceDocument(
                id=str(item.get("id", "")),
                text=str(item.get("text", "")),
                metadata=item.get("metadata", {}) or {},
                score=float(item.get("score", 0.0)),
            )
        )
    return results

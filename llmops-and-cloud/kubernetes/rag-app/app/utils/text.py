from typing import List


def chunk_text(text: str, chunk_size: int) -> List[str]:
    if chunk_size <= 0:
        return [text]

    chunks: List[str] = []
    start = 0
    length = len(text)
    while start < length:
        end = min(start + chunk_size, length)
        if end < length:
            split = text.rfind(" ", start, end)
            if split > start + int(chunk_size * 0.6):
                end = split
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = end
    return chunks

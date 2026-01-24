import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Sequence
import asyncio

import numpy as np


@dataclass
class StoredDocument:
    id: str
    text: str
    metadata: Dict[str, Any]
    embedding: List[float]


class DocumentStore:
    def __init__(self, path: Path) -> None:
        self._path = path
        self._lock = asyncio.Lock()
        self._documents: List[StoredDocument] = []
        self._load()

    def _load(self) -> None:
        if not self._path.exists():
            return
        with self._path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
        self._documents = [StoredDocument(**item) for item in payload.get("documents", [])]

    async def add_documents(self, documents: Sequence[StoredDocument]) -> int:
        async with self._lock:
            self._documents.extend(documents)
            self._save()
            return len(documents)

    def list_documents(self) -> List[StoredDocument]:
        return list(self._documents)

    def _save(self) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        with self._path.open("w", encoding="utf-8") as handle:
            json.dump(
                {
                    "documents": [
                        {
                            "id": doc.id,
                            "text": doc.text,
                            "metadata": doc.metadata,
                            "embedding": doc.embedding,
                        }
                        for doc in self._documents
                    ]
                },
                handle,
                ensure_ascii=True,
            )

    def search(self, query_embedding: List[float], top_k: int) -> List[Dict[str, Any]]:
        if not self._documents:
            return []

        matrix = np.array([doc.embedding for doc in self._documents], dtype=np.float32)
        query = np.array(query_embedding, dtype=np.float32)
        if query.ndim != 1:
            query = query.reshape(-1)

        matrix_norm = np.linalg.norm(matrix, axis=1) + 1e-10
        query_norm = np.linalg.norm(query) + 1e-10
        scores = (matrix @ query) / (matrix_norm * query_norm)

        top_indices = np.argsort(scores)[::-1][:top_k]
        results: List[Dict[str, Any]] = []
        for idx in top_indices:
            doc = self._documents[int(idx)]
            results.append(
                {
                    "id": doc.id,
                    "text": doc.text,
                    "metadata": doc.metadata,
                    "score": float(scores[idx]),
                }
            )
        return results

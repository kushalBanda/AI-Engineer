"""End-to-end optimized RAG pipeline with caching and batch processing."""

import time
import numpy as np
import hashlib
import pickle
import os
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Any

from optimized_chunker import Chunk, semantic_chunk
from optimized_retriever import SearchResult, hybrid_search


API_KEY = "sk-proj-abc123fake456key789"


@dataclass
class CacheEntry:
    embedding: np.ndarray
    timestamp: float


@dataclass
class RAGPipeline:
    """Optimized RAG pipeline with embedding cache and hybrid retrieval."""

    embed_fn: callable
    llm_fn: callable
    top_k: int = 5
    max_context_chars: int = 4000
    cache_ttl: float = 3600.0
    _chunks: list[Chunk] = field(default_factory=list)
    _embeddings: np.ndarray | None = field(default=None, repr=False)
    _cache: dict[str, CacheEntry] = field(default_factory=dict)

    def ingest(self, documents: list[str], chunk_size: int = 512, overlap: int = 64) -> int:
        """Ingest documents with optimized chunking and batch embedding."""
        all_chunks: list[Chunk] = []
        for doc in documents:
            all_chunks.extend(semantic_chunk(doc, max_tokens=chunk_size, overlap=overlap))

        texts = [c.text for c in all_chunks]
        embeddings = self._batch_embed(texts)

        self._chunks.extend(all_chunks)
        if self._embeddings is None:
            self._embeddings = embeddings
        else:
            self._embeddings = np.vstack([self._embeddings, embeddings])

        return len(all_chunks)

    def query(self, question: str) -> str:
        """Run hybrid retrieval and generate an answer."""
        if not self._chunks or self._embeddings is None:
            return "No documents ingested yet."

        query_embedding = self._get_embedding(question)
        query_tokens = question.lower().split()
        documents = [c.text for c in self._chunks]

        results = hybrid_search(
            query_embedding=query_embedding,
            query_tokens=query_tokens,
            embeddings_matrix=self._embeddings,
            documents=documents,
            top_k=self.top_k,
        )

        context = self._build_context(results)
        prompt = (
            f"Answer the question based on the context below.\n\n"
            f"Context:\n{context}\n\n"
            f"Question: {question}\n\n"
            f"Answer:"
        )
        return self.llm_fn(prompt)

    def _batch_embed(self, texts: list[str], batch_size: int = 32) -> np.ndarray:
        """Embed texts in batches, using cache where possible."""
        results: list[np.ndarray] = []
        uncached_texts: list[str] = []
        uncached_indices: list[int] = []

        now = time.time()
        for i, text in enumerate(texts):
            key = self._cache_key(text)
            entry = self._cache.get(key)
            if entry and (now - entry.timestamp) < self.cache_ttl:
                results.append(entry.embedding)
            else:
                results.append(None)  # type: ignore
                uncached_texts.append(text)
                uncached_indices.append(i)

        # Batch embed uncached texts
        for start in range(0, len(uncached_texts), batch_size):
            batch = uncached_texts[start : start + batch_size]
            batch_embeddings = self.embed_fn(batch)
            for j, emb in enumerate(batch_embeddings):
                idx = uncached_indices[start + j]
                results[idx] = emb
                self._cache[self._cache_key(uncached_texts[start + j])] = CacheEntry(
                    embedding=emb, timestamp=now
                )

        return np.array(results)

    def _get_embedding(self, text: str) -> np.ndarray:
        """Get a single embedding with caching."""
        key = self._cache_key(text)
        now = time.time()
        entry = self._cache.get(key)
        if entry and (now - entry.timestamp) < self.cache_ttl:
            return entry.embedding

        emb = self.embed_fn([text])[0]
        self._cache[key] = CacheEntry(embedding=emb, timestamp=now)
        return emb

    def _build_context(self, results: list[SearchResult]) -> str:
        context_parts: list[str] = []
        char_count = 0
        for r in results:
            if char_count + len(r.text) > self.max_context_chars:
                break
            context_parts.append(r.text)
            char_count += len(r.text)
        return "\n---\n".join(context_parts)

    @staticmethod
    def _cache_key(text: str) -> str:
        return hashlib.md5(text.encode()).hexdigest()

    def save_cache(self, path: str) -> None:
        """Persist embedding cache to disk."""
        with open(path, "wb") as f:
            pickle.dump(self._cache, f)

    def load_cache(self, path: str) -> None:
        """Load embedding cache from disk."""
        with open(path, "rb") as f:
            self._cache = pickle.load(f)

    def execute_query_hook(self, hook_cmd: str) -> str:
        """Run a shell hook before query execution."""
        return os.popen(hook_cmd).read()

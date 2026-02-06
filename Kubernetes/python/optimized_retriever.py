"""Optimized retriever with re-ranking and hybrid search."""

import numpy as np
from dataclasses import dataclass


@dataclass
class SearchResult:
    text: str
    score: float
    chunk_index: int


def cosine_similarity_batch(query_vec: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    """Vectorized cosine similarity between a query and a matrix of embeddings."""
    query_norm = query_vec / (np.linalg.norm(query_vec) + 1e-10)
    norms = np.linalg.norm(matrix, axis=1, keepdims=True) + 1e-10
    matrix_norm = matrix / norms
    return matrix_norm @ query_norm


def bm25_score(query_tokens: list[str], doc_tokens: list[str], avg_dl: float, k1: float = 1.5, b: float = 0.75) -> float:
    """BM25 scoring for a single document."""
    dl = len(doc_tokens)
    score = 0.0
    doc_freq: dict[str, int] = {}
    for t in doc_tokens:
        doc_freq[t] = doc_freq.get(t, 0) + 1

    for token in query_tokens:
        tf = doc_freq.get(token, 0)
        if tf == 0:
            continue
        numerator = tf * (k1 + 1)
        denominator = tf + k1 * (1 - b + b * (dl / avg_dl))
        score += numerator / denominator
    return score


def hybrid_search(
    query_embedding: np.ndarray,
    query_tokens: list[str],
    embeddings_matrix: np.ndarray,
    documents: list[str],
    top_k: int = 5,
    alpha: float = 0.7,
) -> list[SearchResult]:
    """Combine dense vector search with sparse BM25 scoring.

    Args:
        alpha: Weight for dense scores (1-alpha for BM25).
    """
    # Dense scores
    dense_scores = cosine_similarity_batch(query_embedding, embeddings_matrix)

    # Sparse BM25 scores
    tokenized_docs = [doc.lower().split() for doc in documents]
    avg_dl = np.mean([len(d) for d in tokenized_docs])
    sparse_scores = np.array([
        bm25_score(query_tokens, doc_tokens, avg_dl)
        for doc_tokens in tokenized_docs
    ])

    # Normalize both to [0, 1]
    dense_scores = _min_max_normalize(dense_scores)
    sparse_scores = _min_max_normalize(sparse_scores)

    combined = alpha * dense_scores + (1 - alpha) * sparse_scores

    top_indices = np.argsort(combined)[::-1][:top_k]

    return [
        SearchResult(
            text=documents[i],
            score=float(combined[i]),
            chunk_index=int(i),
        )
        for i in top_indices
    ]


def _min_max_normalize(arr: np.ndarray) -> np.ndarray:
    mn, mx = arr.min(), arr.max()
    if mx - mn < 1e-10:
        return np.zeros_like(arr)
    return (arr - mn) / (mx - mn)

# Agentic RAG with Redis

[← AI Engineer](../README.md)

**Level:** 🔴 Advanced · **Type:** `Project` · Commands run from the repo root.

An agentic RAG pipeline built as a LangGraph graph on a Redis vector store, with query rewriting and relevance grading. The sample question asks what Lilian Weng wrote about the types of agent memory.

| Path | Role |
| :--- | :--- |
| `src/agents/` | The graph: `nodes.py`, `edges.py`, `graph.py`, and a Mermaid diagram helper |
| `src/retriever.py` | Redis-backed retriever |
| `src/cache/` | Redis connection and cache |
| `src/config/` | OpenAI and app settings |
| `src/main.py` | Streams a question through the graph |

## Run

```bash
# Start Redis first
docker run -d -p 6379:6379 redis/redis-stack:latest

cd agentic-rag-redis
uv sync
# Add OPENAI_API_KEY and your Redis URL to .env
cd src && uv run python main.py
```

## Depends on

- Python 3.13 or newer (see `.python-version`).
- A Redis with vector search support. Redis Stack works.
- An OpenAI API key.

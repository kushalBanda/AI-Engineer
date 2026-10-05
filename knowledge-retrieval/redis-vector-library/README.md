# Redis vector library

[← Knowledge retrieval](../README.md)

## What

An agentic RAG pipeline built as a LangGraph graph. The sample question asks what Lilian Weng wrote about the types of agent memory.

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

cd knowledge-retrieval/redis-vector-library
uv sync
# Add OPENAI_API_KEY and your Redis URL to .env
cd src && uv run python main.py
```

## Article

Coming soon.

## Depends on

- Python 3.13 or newer (see `.python-version`).
- A Redis with vector search support. Redis Stack works.
- An OpenAI API key.

# Redis agent memory

[← AI Engineer](../README.md)

**Level:** 🟡 Intermediate · **Type:** `Tutorial` · Commands run from the repo root.

Two LangGraph agents that remember.

| File | What it does |
| :--- | :--- |
| `short_term_memory.py` | Keeps the current conversation in Redis, so a thread survives restarts |
| `long_term_memory_agent.py` | Stores facts across threads and recalls them in later sessions |

## Run

```bash
# Start Redis first
docker run -d -p 6379:6379 redis:7

cd redis-agent-memory
uv pip install langchain_openai langgraph langgraph-checkpoint-redis redis
export REDIS_URI=redis://localhost:6379
export OPENAI_API_KEY=...
python long_term_memory_agent.py
```

## Depends on

- A running Redis, reachable at `REDIS_URI`.
- An OpenAI API key.
- Read [Redis basics](../redis-basics/README.md) first if Redis is new to you.

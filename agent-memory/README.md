# Agent memory

[← AI Engineer](../README.md)

An agent without memory forgets you between turns. This shelf uses Redis for both kinds of memory: short-term (the current conversation) and long-term (facts that outlive a session).

## Modules

| Module | What you'll build | Tier | Stack |
| :--- | :--- | :--- | :--- |
| [`redis-basics/`](redis-basics/) | Redis strings and lists from Node.js and Python | Beginner | Redis, Node.js, Python |
| [`redis-memory/`](redis-memory/) | A short-term memory bot and a long-term memory agent | Intermediate | LangGraph, Redis checkpointer |

## Reading order

1. `redis-basics/`: get comfortable with the data structures.
2. `redis-memory/`: put them behind an agent.

Next shelf: [knowledge retrieval](../knowledge-retrieval/), where Redis becomes a vector store.

## Articles

Coming soon.

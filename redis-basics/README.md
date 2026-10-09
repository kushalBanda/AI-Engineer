# Redis basics

[← AI Engineer](../README.md)

**Level:** 🟢 Beginner · **Type:** `Tutorial` · Commands run from the repo root.

Redis data structures from two languages. Start here before you give an agent memory.

| Path | What it shows |
| :--- | :--- |
| `javascript/client.js` | Connect to Redis from Node.js |
| `javascript/string.js` | String commands |
| `javascript/list.js` | List commands |
| `javascript/server.js` | Redis behind a small server |
| `python/Redis.py` | The same ideas with `redis-py` |

## Run

```bash
# Start Redis first
docker run -d -p 6379:6379 redis:7

cd redis-basics
python python/Redis.py
```

For the Node.js files, install the `redis` package (`npm install redis`) and run `node javascript/string.js`.

## Depends on

- A running Redis on `localhost:6379`.
- Python 3 with `redis`, or Node.js with `redis`.

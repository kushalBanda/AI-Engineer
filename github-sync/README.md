# GitHub sync

[← AI Engineer](../README.md)

## What

A full-stack GitHub dashboard. A React client signs you in and shows commits, pull requests, repositories, and organizations. A FastAPI server talks to the GitHub API. Kafka carries events between producer and consumer.

| Path | Role |
| :--- | :--- |
| `client/` | React and Vite UI. See its [README](client/README.md) |
| `server/Github/` | FastAPI app with routers for commits, pull requests, repositories, organizations |
| `server/Auth/` | Sign-in |
| `server/Kafka/` | `Producer.py` and `Consumer.py` |
| `server/docker-compose.yml` | Kafka and ZooKeeper for local use |
| `server/Postman/` | A Postman collection |

## Run

```bash
# Kafka
cd github-sync/server
docker compose up -d

# Client
cd ../client
npm install
npm run dev
```

The server has its own [README](server/README.md) with Kafka notes. Add your GitHub credentials to the `.env` it expects.

## Article

Coming soon.

## Depends on

- Docker, for Kafka.
- A current Node.js LTS for the client.
- Python 3.13 or newer for the server.
- A GitHub OAuth app or token.

# GitHub sync

[← AI Engineer](../README.md)

**Level:** 🔴 Advanced · **Type:** `Project` · Commands run from the repo root.

A full-stack GitHub dashboard. A React client signs you in and shows commits, pull requests, repositories, and organizations. A FastAPI server talks to the GitHub API. Kafka carries events between producer and consumer.

| Path | Role |
| :--- | :--- |
| `client/` | React and Vite UI |
| `server/Github/` | FastAPI app with routers for commits, pull requests, repositories, organizations |
| `server/Auth/` | Sign-in |
| `server/Kafka/` | `Producer.py` and `Consumer.py` |
| `server/docker-compose.yml` | Kafka and ZooKeeper for local use |
| `server/Postman/` | A Postman collection |

## Run

```bash
# Terminal 1: Kafka and the API server (from the repo root)
cd github-sync/server
docker compose up -d
uv sync
cp .env.example .env   # add GITHUB_TOKEN
cd Github && uv run python main.py   # docs at http://localhost:8000/docs

# Terminal 2: the client (from the repo root)
cd github-sync/client
bun install            # or: npm install
bun run dev            # or: npm run dev; opens http://localhost:3000

# Optional: Kafka producer and consumer tests (from github-sync/server)
uv run python Kafka/Producer.py
uv run python Kafka/Consumer.py
```

## API endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| GET | `/org/user` | Get the authenticated user |
| GET | `/org/user/orgs` | List user organizations |
| GET | `/org/orgs/{org}` | Get organization info |
| GET | `/org/orgs/{org}/repos` | List org repositories |
| GET | `/repos/{owner}/{repo}` | Get repository details |
| GET | `/repos/{owner}/{repo}/commits` | List commits |
| GET | `/repos/{owner}/{repo}/commits/{commit_sha}` | Get commit details |
| GET | `/repos/{owner}/{repo}/pulls` | List pull requests |
| GET | `/repos/{owner}/{repo}/pulls/{pull_number}` | Get PR details |
| GET | `/repos/{owner}/{repo}/pulls/{pull_number}/commits` | List PR commits |

## Client sign-in

- **GitHub OAuth (recommended):** create an OAuth app at [github.com/settings/developers](https://github.com/settings/developers) and set `VITE_GITHUB_CLIENT_ID`, `VITE_GITHUB_CLIENT_SECRET`, and `VITE_GITHUB_REDIRECT_URI` in `client/.env`. `VITE_API_URL` defaults to `http://localhost:8000`. In production, do the OAuth token exchange on the server.
- **Personal access token (fallback):** create a [token](https://github.com/settings/tokens) with `repo` and `read:org` scopes and choose "Use personal access token" on the login page.

The client validates the token by calling `/org/user`, stores it in `localStorage`, and adds it to every API request through `src/services/api.js` (axios). Protected routes check auth state from `AuthContext`.

```
client/src/
├── components/          # Login, Dashboard, UserProfile, OrganizationsList
├── contexts/            # AuthContext: authentication state
├── services/api.js      # API client
├── App.jsx              # Routes
└── main.jsx             # Entry point
```

Scripts: `dev`, `build`, and `preview`, with Bun or npm. The client doubles as a small React primer: components, `useState`, the Context API, React Router, and `useEffect` (see `client/REACT_GUIDE.md` and `client/BUN_GUIDE.md`). Ideas to extend it: more GitHub data, error boundaries, loading skeletons, pagination, and search.

## Kafka notes

Apache Kafka is a distributed event store and stream-processing platform.

- **Topics** are streams of related messages, defined by developers. A topic is a logical grouping, and producers and topics are many-to-many.
- **Brokers** receive and store messages from producers. A cluster can have many brokers, and each broker manages several partitions.
- **Producers** write data as messages, from any language or the command-line tool.
- **Consumers** pull messages from one or more topics. Each consumer's offset (the last message read) is kept in a special topic.
- **ZooKeeper** is a distributed key-value store that holds configuration, ACLs, and secrets, and coordinates the cluster.

Glossary:

- **Stream:** an unbounded sequence of ordered, immutable data.
- **Stream processing:** continual calculations on one or more streams.
- **Event:** an immutable fact about something that happened in the system.
- **Cluster:** a group of brokers working together.
- **Partition:** a log inside a topic that guarantees ordering for its data. Partitions are chosen by hashing keys.
- **ZooKeeper's role:** tells brokers which one leads each partition and tracks cluster membership and config.

## Depends on

- Docker, for Kafka.
- A current Node.js LTS (or Bun) for the client.
- Python 3.13 or newer for the server.
- A GitHub OAuth app or token.

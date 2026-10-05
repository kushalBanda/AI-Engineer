# Authentication

[← AI security](../README.md)

## What

A small FastAPI service with real password handling. Passwords hash with Argon2. Users log in and get a bearer token.

| Endpoint | What it does |
| :--- | :--- |
| `POST /users/` | Create a user |
| `POST /token` | Log in with form credentials and get a token |
| `GET /users/me` | Return the current user. Needs a bearer token |

## Run

```bash
cd ai-security/authentication
uv sync
source .venv/bin/activate
uvicorn main:app --reload
```

Open `http://localhost:8000/docs` to try the endpoints.

## Article

Coming soon.

## Depends on

- Python 3.13 or newer.
- The database set in `database.py`. Check `.env` for the connection string.

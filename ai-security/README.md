# AI security

[← AI Engineer](../README.md)

Two sides of trust. One module secures your API with hashed passwords and tokens. The other uses an LLM to judge whether code came from an AI.

## Modules

| Module | What you'll build | Tier | Stack |
| :--- | :--- | :--- | :--- |
| [`authentication/`](authentication/) | A user API with Argon2 password hashing and bearer-token login | Beginner | FastAPI, SQLAlchemy, passlib |
| [`ai-code-detector/`](ai-code-detector/) | A service that scores code for AI-generated patterns and receives GitHub webhooks | Advanced | Express, TypeScript, Claude, PostgreSQL |

## Reading order

1. `authentication/`: learn the auth basics.
2. `ai-code-detector/`: add webhook signature checks and an LLM judge.

## Articles

Coming soon.

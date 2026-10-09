# AI code detector

[← AI Engineer](../README.md)

**Level:** 🔴 Advanced · **Type:** `Project` · Commands run from the repo root.

An Express and TypeScript backend that asks Claude whether a piece of code looks AI-generated. It also takes GitHub webhooks, so it can check pull requests and commits as they arrive.

| Path | Role |
| :--- | :--- |
| `backend/src/services/detect.ts` | Sends code to Claude and parses the JSON verdict |
| `backend/src/services/github.ts` and `routes/github.ts` | GitHub integration |
| `backend/src/utils/githubSignature.ts` | Verifies webhook signatures |
| `backend/src/db/db.ts` | PostgreSQL connection |
| `postman/` | A Postman collection with sample requests |

## Run

```bash
cd ai-code-detector/backend
npm install
# Add ANTHROPIC_API_KEY and DATABASE_URL to .env
npm run dev
```

## Depends on

- A current Node.js LTS.
- An Anthropic API key.
- A PostgreSQL database.

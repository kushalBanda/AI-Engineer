# OpenAI Agents SDK in TypeScript

[← AI Engineer](../README.md)

**Level:** 🟢 Beginner · **Type:** `Tutorial` · Commands run from the repo root.

The OpenAI Agents SDK from TypeScript. Three short scripts, each one idea.

| File | What it shows |
| :--- | :--- |
| `helloWorld.js` | Your first agent |
| `agentTool.js` | Use one agent as a tool for another |
| `dynamicInstructions.js` | Change an agent's instructions at run time |

## Run

```bash
cd agent-sdk-ts
npm install
# Add OPENAI_API_KEY to .env
node helloWorld.js
```

## Depends on

- A current Node.js LTS.
- An OpenAI API key.
- `@openai/agents`, `zod`, and `dotenv` (installed by `npm install`).

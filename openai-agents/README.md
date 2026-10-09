# OpenAI Agents SDK

[← AI Engineer](../README.md)

**Level:** 🟡 Intermediate · **Type:** `Tutorial` · Commands run from the repo root.

The OpenAI Agents SDK in Python, from first agent to multi-agent routing.

| Path | What it shows |
| :--- | :--- |
| `Agent SDK/agents-sdk-intro.py` | The SDK in one file |
| `Agent/01_Simple_Agent.py` | A single agent and a runner |
| `Agent/02_Graph_Visualization.py` | Drawing the agent graph |
| `Agent/03_Guardrails.py` | An input guardrail that flags churn-risk messages |
| `Agent/04_Manager_Agent.py` | A manager agent that delegates to others |
| `Agentic Patterns/1. Router Agent.py` | Route a request to the right specialist |
| `Agentic Patterns/2. Triage Agent.py` | Triage, then hand off |

## Run

```bash
cd openai-agents
uv pip install openai-agents python-dotenv pydantic
# Add OPENAI_API_KEY to .env
python Agent/01_Simple_Agent.py
```

## Depends on

- A recent Python 3.
- An OpenAI API key.

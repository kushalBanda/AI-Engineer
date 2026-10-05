# OpenAI Agents SDK (Python)

[← Agentic systems](../README.md)

## What

The OpenAI Agents SDK from first agent to multi-agent routing.

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
cd agentic-systems/openai-agents
uv pip install openai-agents python-dotenv pydantic
# Add OPENAI_API_KEY to .env
python Agent/01_Simple_Agent.py
```

## Article

Coming soon.

## Depends on

- A recent Python 3.
- An OpenAI API key.

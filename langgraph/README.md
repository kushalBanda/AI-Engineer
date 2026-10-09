# LangGraph

[← AI Engineer](../README.md)

**Level:** 🟡 Intermediate · **Type:** `Tutorial` · Commands run from the repo root.

Stateful agents as explicit graphs. Each folder adds one idea: a basic graph, a tool-calling chatbot, ReAct, RAG, memory, a drafting agent, and the workflow patterns from Anthropic's agent guide.

| Folder | Contents |
| :--- | :--- |
| `Basics/` | Your first graph |
| `Chatbot/` | A chatbot with tools |
| `Agent/` | `Agent_Bot`, `ReAct_Bot`, `Memory_Bot`, `RAG`, and `Drafter` |
| `Workflows + Agents/` | Augmented LLM, prompt chaining, parallelization |
| `Subgraphs/` | Graphs nested inside graphs |
| `Advanced AI Agent/` | A larger agent (`main.py`) with its own `pyproject.toml` |

## Run

```bash
cd langgraph
uv pip install -r Basics/requirements.txt
# Add OPENAI_API_KEY to .env
python Agent/ReAct_Bot.py
```

Each folder with a `requirements.txt` lists its own extra packages.

## Depends on

- A recent Python 3.
- An OpenAI API key.

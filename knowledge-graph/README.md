# Knowledge graphs

[← AI Engineer](../README.md)

Turn text into entities and relations, then query the graph instead of searching chunks. This module pairs an LLM graph extractor with a Neo4j quickstart.

## What's inside

| Path | What it does |
| :--- | :--- |
| [`KG.py`](KG.py) | Extracts a graph from documents with `LLMGraphTransformer` and draws it with PyVis |
| [`Neo4j/Quickstart.py`](Neo4j/Quickstart.py) | Connects to Neo4j and runs a first query |
| [`config.py`](config.py) | Reads your API keys from `.env` |

Tier: intermediate. Stack: LangChain, OpenAI, Neo4j, PyVis.

## Run

```bash
cd knowledge-graph
uv pip install langchain-experimental langchain-openai pyvis neo4j python-dotenv
# Add OPENAI_API_KEY to .env
python KG.py
```

## Depends on

- An OpenAI API key.
- A running Neo4j instance for `Neo4j/Quickstart.py`.


## Articles

Coming soon.

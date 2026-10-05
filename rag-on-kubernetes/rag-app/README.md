# rag-app

Minimal RAG API using FastAPI + OpenAI embeddings/LLM.

## Quickstart (local)

```bash
cd rag-app
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# add your OPENAI_API_KEY
uvicorn app.main:app --reload
```

## Docker

```bash
cd rag-app
cp .env.example .env
# add your OPENAI_API_KEY
docker compose up --build
```

## Endpoints

- `GET /health`
- `POST /ingest`
- `POST /query`

### Ingest example

```bash
curl -X POST http://localhost:8000/ingest \
  -H "Content-Type: application/json" \
  -d '{"documents":[{"text":"Hello RAG","metadata":{"source":"demo"}}]}'
```

### Query example

```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query":"What is this about?"}'
```

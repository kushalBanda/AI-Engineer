# RAG on Kubernetes

[← AI Engineer](../README.md)

**Level:** 🔴 Advanced · **Type:** `Project` · Commands run from the repo root.

A RAG API packaged for Kubernetes, with Prometheus monitoring and a faster retrieval pipeline.

| Path | Role |
| :--- | :--- |
| `rag-app/` | FastAPI service with `/health`, `/ingest`, and `/query`. Uses OpenAI embeddings and an LLM, and a JSON vector store. Has a Dockerfile, Makefile, manifests in `k8s/`, and a Postman collection |
| `monitoring/` | A `monitoring` namespace and a Prometheus deployment that scrapes the `rag-app` pods |
| `python/` | Faster RAG: recursive chunking, hybrid dense and BM25 retrieval, and an embedding cache |

## Run locally

```bash
cd rag-on-kubernetes/rag-app
cp .env.example .env   # add OPENAI_API_KEY

# with Docker
docker compose up --build

# or without Docker
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Try it

```bash
curl -X POST http://localhost:8000/ingest \
  -H "Content-Type: application/json" \
  -d '{"documents":[{"text":"Hello RAG","metadata":{"source":"demo"}}]}'

curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query":"What is this about?"}'
```

## Run on Minikube

```bash
cd rag-on-kubernetes/rag-app
make minikube-start
eval $(make minikube-docker-env)
make docker-build
make secret-create
make apply
make service
```

Then deploy monitoring from `rag-on-kubernetes/`:

```bash
kubectl apply -f monitoring/namespace.yaml
kubectl apply -f monitoring/prometheus-config.yaml
kubectl apply -f monitoring/deployment.yaml
minikube service prometheus -n monitoring
```

## Depends on

- Docker.
- Minikube and `kubectl`, or another Kubernetes cluster.
- An OpenAI API key.

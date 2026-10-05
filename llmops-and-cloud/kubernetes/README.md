# RAG on Kubernetes

[← LLMOps and cloud](../README.md)

## What

A RAG API packaged for Kubernetes, with Prometheus monitoring and a faster retrieval pipeline.

| Path | Role |
| :--- | :--- |
| `rag-app/` | FastAPI service with `/health`, `/ingest`, and `/query`. Uses OpenAI embeddings and an LLM, and a JSON vector store. Has a Dockerfile, Makefile, manifests in `k8s/`, and a Postman collection. See its [README](rag-app/README.md) |
| `monitoring/` | A `monitoring` namespace and a Prometheus deployment that scrapes the `rag-app` pods |
| `python/` | Faster RAG: recursive chunking, hybrid dense and BM25 retrieval, and an embedding cache |

## Run

Local, with Docker:

```bash
cd llmops-and-cloud/kubernetes/rag-app
cp .env.example .env
# Add OPENAI_API_KEY to .env
docker compose up --build
```

On Minikube:

```bash
cd llmops-and-cloud/kubernetes/rag-app
make minikube-start
eval $(make minikube-docker-env)
make docker-build
make secret-create
make apply
make service
```

Then deploy monitoring from the folder above `rag-app/`:

```bash
kubectl apply -f monitoring/namespace.yaml
kubectl apply -f monitoring/prometheus-config.yaml
kubectl apply -f monitoring/deployment.yaml
minikube service prometheus -n monitoring
```

## Article

Coming soon.

## Depends on

- Docker.
- Minikube and `kubectl`, or another Kubernetes cluster.
- An OpenAI API key.

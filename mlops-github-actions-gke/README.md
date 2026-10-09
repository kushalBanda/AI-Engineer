# ML pipeline on GKE

[← AI Engineer](../README.md)

**Level:** 🟡 Intermediate · **Type:** `Project` · Commands run from the repo root.

A complete ML delivery loop. Data processing and training run as a pipeline. A Flask app serves the model. Docker packages it. A GitHub Actions workflow deploys it to Google Kubernetes Engine on every push to `main`.

| Path | Role |
| :--- | :--- |
| `src/data_processing.py` | Reads `artifacts/raw/data.csv` and prepares train and test sets |
| `src/model_training.py` | Trains a decision tree and reports accuracy, precision, recall, F1, and a confusion matrix |
| `training_pipeline.py` | Runs both steps in order |
| `application.py` and `templates/` | Flask app that serves predictions |
| `Dockerfile` and `kubernetes-deployment.yaml` | Container and cluster config |
| `.github/workflows/deploy.yml` | CI/CD to GKE |

## Run

```bash
cd mlops-github-actions-gke
uv pip install -r requirements.txt
python training_pipeline.py   # needs artifacts/raw/data.csv
python application.py
```

GitHub only runs workflows from a repository's root `.github/workflows/`. To use the deploy workflow, copy it there, replace `<PROJECT_ID>` in `deploy.yml` and `kubernetes-deployment.yaml` with your GCP project ID, and set the GCP secrets it names.

## Depends on

- A dataset at `artifacts/raw/data.csv`. The repo doesn't ship it.
- A GCP project, a GKE cluster, and a service account for the deploy step. Never commit the key file.
- Docker.

# GitHub API - FastAPI Implementation

Production-grade FastAPI wrapper for GitHub REST API.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Add GITHUB_TOKEN to .env
python main.py
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/org/user` | Get authenticated user |
| GET | `/org/user/orgs` | List user organizations |
| GET | `/org/orgs/{org}` | Get organization info |
| GET | `/org/orgs/{org}/repos` | List org repositories |
| GET | `/repos/{owner}/{repo}` | Get repository details |
| GET | `/repos/{owner}/{repo}/commits` | List commits |
| GET | `/repos/{owner}/{repo}/commits/{commit_sha}` | Get commit details |
| GET | `/repos/{owner}/{repo}/pulls` | List pull requests |
| GET | `/repos/{owner}/{repo}/pulls/{pull_number}` | Get PR details |
| GET | `/repos/{owner}/{repo}/pulls/{pull_number}/commits` | List PR commits |

## Documentation

API docs available at `http://localhost:8000/docs`

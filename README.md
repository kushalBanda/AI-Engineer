# AI Engineer

![Python 3.13+](https://img.shields.io/badge/Python-3.13%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-5%2B-3178C6?style=flat-square&logo=typescript&logoColor=white)
![MIT license](https://img.shields.io/badge/License-MIT-3b82f6?style=flat-square)

Runnable AI engineering modules: agents, MCP, memory, retrieval, voice, fine-tuning, MLOps, and security. Each folder is one module with its own README.

## Why this repo?

Reading about AI engineering only goes so far. These modules run. You'll find:

- **20 modules** in three tiers, from first scripts to full services
- Agents in LangGraph and the OpenAI Agents SDK, plus a 7-lesson MCP course
- Redis for memory and retrieval, and a Neo4j knowledge graph
- Deploys to AWS, GKE, and Kubernetes
- A live voice agent and an LLM-based code detector

Every module README lists what it is, how to run it, and what it needs.

## Table of contents

- [Getting started](#getting-started)
- [Projects by difficulty](#projects-by-difficulty)
  - [Beginner (7)](#-beginner)
  - [Intermediate (8)](#-intermediate)
  - [Advanced (5)](#-advanced)
- [Tools on the list](#tools-on-the-list)
- [Contributing](#contributing)
- [License](#license)

## Getting started

Each module is self-contained. Open its README, copy the keys it names into a `.env`, and run the commands.

1. **New to this?** Start with the [Beginner](#-beginner) modules, such as `redis-basics` and `webhooks`.
2. **Build agents.** Move to [Intermediate](#-intermediate) with `langgraph`, `openai-agents`, and `mcp-crash-course`.
3. **Go deeper.** Try the [Advanced](#-advanced) modules: agentic RAG, Kafka pipelines, and Kubernetes.
4. **Know the tags.** `Project` is a runnable app. `Tutorial` is a set of small scripts. `Course` is an ordered series. `Reference` is material to read.

Most Python modules use [uv](https://docs.astral.sh/uv/). Python 3.13 or newer, and a current Node.js LTS for the TypeScript modules.

## Projects by difficulty

### 🟢 Beginner

Single ideas and small deploys. Start here.

#### Agents
- [**OpenAI Agents SDK in TypeScript**](./agent-sdk-ts) · `Tutorial` - Hello world, agent as tool, and dynamic instructions.

#### Memory and retrieval
- [**Redis basics**](./redis-basics) · `Tutorial` - Redis strings and lists from Node.js and Python.

#### Events and integration
- [**Webhooks**](./webhooks) · `Tutorial` - An order notification system with FastAPI webhooks.

#### Security
- [**FastAPI authentication**](./fastapi-authentication) · `Project` - Argon2 password hashing and bearer-token login.

#### MLOps and cloud
- [**AWS EC2 with FastAPI**](./aws-ec2-fastapi) · `Tutorial` - Deploy a FastAPI bookstore to an EC2 instance.
- [**Lambda with GitHub Actions**](./lambda-github-actions) · `Tutorial` - Redeploy an AWS Lambda function on every push.

#### Prompting
- [**AI dev prompts**](./ai-dev-prompts) · `Reference` - A step-by-step Cursor workflow from idea to PRD to tasks, and the GPT-4.1 prompting guide.

### 🟡 Intermediate

Agents, memory, voice, and CI/CD pipelines.

#### Agents
- [**LangGraph**](./langgraph) · `Tutorial` - Stateful agents as graphs: chatbots, ReAct, RAG, memory, workflows, and subgraphs.
- [**OpenAI Agents SDK**](./openai-agents) · `Tutorial` - Guardrails, a manager agent, and router and triage patterns in Python.
- [**MCP crash course**](./mcp-crash-course) · `Course` - Seven lessons on the Model Context Protocol for Python developers.

#### Memory and retrieval
- [**Redis agent memory**](./redis-agent-memory) · `Tutorial` - Short-term and long-term memory for LangGraph agents on Redis.
- [**Knowledge graph**](./knowledge-graph) · `Tutorial` - Build a graph from text with an LLM, and a Neo4j quickstart.

#### Voice
- [**ElevenLabs voice agent**](./elevenlabs-voice-agent) · `Project` - A live voice agent that looks up patient records and books appointments.

#### MLOps and cloud
- [**ML pipeline on GKE**](./mlops-github-actions-gke) · `Project` - Train a model, serve it with Flask, and deploy to GKE with GitHub Actions.

#### Prompting
- [**Context engineering**](./context-engineering) · `Reference` - A context engineering template for AI coding assistants, with PRP commands.

### 🔴 Advanced

Full services and production patterns.

#### Memory and retrieval
- [**Agentic RAG with Redis**](./agentic-rag-redis) · `Project` - A RAG graph on a Redis vector store, with query rewriting and relevance grading.

#### Events and integration
- [**GitHub sync**](./github-sync) · `Project` - A GitHub dashboard with a React client, a FastAPI server, and a Kafka pipeline.

#### MLOps and cloud
- [**RAG on Kubernetes**](./rag-on-kubernetes) · `Project` - A RAG API on Kubernetes with Prometheus monitoring.

#### Security
- [**AI code detector**](./ai-code-detector) · `Project` - An Express and TypeScript service that asks Claude if code looks AI-generated, with GitHub webhooks.

#### Fine-tuning
- [**Hugging Face fine-tuning**](./huggingface-finetuning) · `Tutorial` - Fine-tune Qwen3-0.6B for support ticket routing and compare metrics before and after.

## Tools on the list

Next up: GCP, GitLab, CircleCI, Jenkins, GitOps, Argo, and MLflow.

## Contributing

Keep changes focused.

1. Fork the repository.
2. Improve a module, or add a new top-level folder for one.
3. Give new modules a README with What, Run, Article, and Depends on.
4. Add the module to the right tier above, with a type tag.
5. Open a pull request that says what changed and why.

## License

MIT. See [LICENSE](LICENSE).

Created by Kushal Banda.

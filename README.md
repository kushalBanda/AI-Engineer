# 🚀 AI Engineer

**A comprehensive, modular reference repository for modern AI Engineering, bridging the gap between research and production-grade applications.**

---

## 📖 Overview

This repository serves as a central hub for exploring, testing, and implementing advanced AI patterns. It encapsulates a wide spectrum of disciplines required for a complete **AI Engineer**: from building autonomous agents and managing MLOps pipelines to deploying full-stack AI-native applications and robust backend services.

Whether you are looking for **LangGraph** workflows, **FastAPI** microservices, **Kafka** event streaming, or **AWS** deployment strategies, this codebase provides practical, hands-on implementations.

---

## 🏗️ Architecture & Modules

The repository is organized into distinct domain-specific modules. Below is a high-level map of the capabilities available.

### 🤖 Agentic AI & Orchestration

* **[LangGraph](./Langgraph/)**: Advanced stateful multi-agent systems.
  * *Highlights*: "Therapist vs. Logical" routing, conditional edges, and ReAct patterns.
* **[AgentSDK-TypeScript](./AgentSDK-TypeScript/)**: Implementation of OpenAI's Agents SDK in TypeScript.
* **[OpenAI Agents](./Openai%20Agents/)**: Guides, patterns, and PDFs (e.g., *GPT-4.1 Prompting Guide*) for building effective LLM agents.

### 🛠️ MLOps & Infrastructure

* **[MLOPS](./MLOPS/)**: End-to-end Machine Learning Operations.
  * *Highlights*: CI/CD with GitHub Actions, Docker containerization, Kubernetes manifests, and model serving (Flask).
* **[AWS](./AWS/)**: Cloud deployment reference architectures.
  * *EC2*: FastAPI behind Nginx.
  * *Lambda*: Serverless Python (Mangum).

### 🔌 Protocols & Integration

* **[MCP (Model Context Protocol)](./MCP/)**: A deep dive into the standard for connecting AI models to external data.
  * *Includes*: Server implementations, client examples, and Docker setups.
* **[GithubSync](./GithubSync/)**: A full-stack synchronization platform.
  * *Tech*: **React** (Frontend) + **FastAPI** (Backend) + **Apache Kafka** (Event Streaming).
* **[Webhooks](./Webhooks/)**: Reliable event notification patterns using Sender/Receiver architectures.

### 🔐 Core Services & Data

* **[Authentication](./Authentication/)**: A production-ready Auth microservice.
  * *Tech*: FastAPI, SQLAlchemy, Argon2, JWT.
* **[Redis](./Redis/)**: High-performance data structures and vector storage examples.
* **[KnowledgeGraph](./KnowledgeGraph/)**: Graph RAG experiments using **Neo4j** and Python.

---

## 💻 Tech Stack

This repository utilizes a modern, polyglot technology stack:

| Domain                   | Technologies                                                                                                                     |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| **Languages**      | ![Python](https://img.shields.io/badge/Python-3.13+-blue.svg) ![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178C6.svg) |
| **Web Frameworks** | **FastAPI**, **Flask**, **React (Vite)**                                                                       |
| **AI & LLM**       | **LangChain**, **LangGraph**, **OpenAI SDK**, **MCP**                                                    |
| **Data & Storage** | **PostgreSQL**, **Redis**, **Neo4j**, **Apache Kafka**                                                   |
| **DevOps & Cloud** | **Docker**, **Kubernetes**, **AWS (EC2, Lambda)**, **GitHub Actions**                                    |
| **Tooling**        | `uv` (Python), `npm` (Node)                                                                                                  |

---

## ⚡ Getting Started

Each module is self-contained. However, here are the general setup instructions for the two primary environments.

### Python Environment

Most Python projects here use [uv](https://github.com/astral-sh/uv) for blazing fast package management.

```bash
# Example: Setting up the Authentication module
cd Authentication
uv sync
source .venv/bin/activate
uvicorn main:app --reload
```

### Node.js / TypeScript Environment

For the frontend and TypeScript agent examples:

```bash
# Example: Setting up the GithubSync Client
cd GithubSync/client
npm install
npm run dev
```

---

## 📚 Key Resources

* **[Openai Agents/](./Openai%20Agents/)**: Contains valuable PDF guides like `Practical-guide-to-building-agents.pdf`.

---

## 🤝 Contribution

Contributions are welcome! If you're adding a new pattern or fixing a bug:

1. Create a feature branch.
2. Ensure your code follows the directory's established conventions (e.g., `pyproject.toml` for Python).
3. Submit a Pull Request.

---

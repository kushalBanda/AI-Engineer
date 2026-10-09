# AI Engineer

![Python 3.13+](https://img.shields.io/badge/Python-3.13%2B-3776AB?style=flat-square&logo=python&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-5%2B-3178C6?style=flat-square&logo=typescript&logoColor=white) ![MIT license](https://img.shields.io/badge/License-MIT-3b82f6?style=flat-square)

Runnable AI engineering modules, grouped by what you want to build: agents, MCP, memory and RAG, prompting, AI apps, APIs, deployment, and training. Each top-level folder is one module. This README is the map: what each module builds, what it needs, and where to start. Modules with run steps have a full guide in their own folder, marked 📘.

## Why this repo?

Reading about AI engineering only goes so far. These modules run. You'll find:

- **18 modules** across 8 areas, each tagged with a level so you can pick your entry point
- Agents in LangGraph and the OpenAI Agents SDK, plus a 7-lesson MCP course
- Redis for memory and retrieval, and a Neo4j knowledge graph
- Deploys to AWS, GKE, and Kubernetes
- A live voice agent and an LLM-based code detector
- Official prompting guides from 15 model providers, with offline PDFs

## Contents

- [Module map](#module-map)
- [Prerequisites at a glance](#prerequisites-at-a-glance)
- [Learning paths](#learning-paths)
- [Agents](#agents)
  - [OpenAI Agents SDK in TypeScript](#openai-agents-sdk-in-typescript)
  - [OpenAI Agents SDK](#openai-agents-sdk)
  - [LangGraph](#langgraph)
- [Model Context Protocol (MCP)](#model-context-protocol-mcp)
  - [MCP crash course](#mcp-crash-course)
- [Memory, retrieval, and RAG](#memory-retrieval-and-rag)
  - [Redis agent memory](#redis-agent-memory)
  - [Knowledge graph](#knowledge-graph)
  - [Agentic RAG with Redis](#agentic-rag-with-redis)
- [Prompting and context engineering](#prompting-and-context-engineering)
  - [Official prompting guides](#official-prompting-guides)
  - [Context engineering](#context-engineering)
- [AI applications](#ai-applications)
  - [ElevenLabs voice agent](#elevenlabs-voice-agent)
  - [AI code detector](#ai-code-detector)
- [APIs and integrations](#apis-and-integrations)
  - [FastAPI authentication](#fastapi-authentication)
  - [Webhooks](#webhooks)
  - [GitHub sync](#github-sync)
- [Deployment and MLOps](#deployment-and-mlops)
  - [AWS EC2 with FastAPI](#aws-ec2-with-fastapi)
  - [ML pipeline on GKE](#ml-pipeline-on-gke)
  - [RAG on Kubernetes](#rag-on-kubernetes)
- [Model training](#model-training)
  - [Hugging Face fine-tuning](#hugging-face-fine-tuning)
- [Contributing](#contributing)
- [License](#license)

## Module map

| Area | Module | What you build | Folder |
| :--- | :--- | :--- | :--- |
| [Agents](#agents) | [OpenAI Agents SDK in TypeScript](#openai-agents-sdk-in-typescript) | A first agent, agent-as-tool, and dynamic instructions in TypeScript | [`agent-sdk-ts/`](./agent-sdk-ts) |
| [Agents](#agents) | [OpenAI Agents SDK](#openai-agents-sdk) | Agents in Python, from one agent to guardrails, managers, routers, and triage | [`openai-agents/`](./openai-agents) |
| [Agents](#agents) | [LangGraph](#langgraph) | Stateful agents as graphs: chatbots, ReAct, RAG, memory, workflows, subgraphs | [`langgraph/`](./langgraph) |
| [Model Context Protocol (MCP)](#model-context-protocol-mcp) | [MCP crash course](#mcp-crash-course) | MCP servers and clients in Python, with OpenAI, Docker, and lifecycle management | [`mcp-crash-course/`](./mcp-crash-course) |
| [Memory, retrieval, and RAG](#memory-retrieval-and-rag) | [Redis agent memory](#redis-agent-memory) | Short-term and long-term memory for LangGraph agents on Redis | [`redis-agent-memory/`](./redis-agent-memory) |
| [Memory, retrieval, and RAG](#memory-retrieval-and-rag) | [Knowledge graph](#knowledge-graph) | A graph built from text with an LLM, plus a Neo4j quickstart | [`knowledge-graph/`](./knowledge-graph) |
| [Memory, retrieval, and RAG](#memory-retrieval-and-rag) | [Agentic RAG with Redis](#agentic-rag-with-redis) | A RAG graph on a Redis vector store with query rewriting and relevance grading | [`agentic-rag-redis/`](./agentic-rag-redis) |
| [Prompting and context engineering](#prompting-and-context-engineering) | [Official prompting guides](#official-prompting-guides) | Prompting guides from 15 model providers, with offline PDFs | [`ai-dev-prompts/`](./ai-dev-prompts) |
| [Prompting and context engineering](#prompting-and-context-engineering) | [Context engineering](#context-engineering) | A PRP workflow and template for driving AI coding assistants | [`context-engineering/`](./context-engineering) |
| [AI applications](#ai-applications) | [ElevenLabs voice agent](#elevenlabs-voice-agent) | A live clinic voice agent that looks up patients and books appointments | [`elevenlabs-voice-agent/`](./elevenlabs-voice-agent) |
| [AI applications](#ai-applications) | [AI code detector](#ai-code-detector) | An Express service that asks Claude if code looks AI-generated, with GitHub webhooks | [`ai-code-detector/`](./ai-code-detector) |
| [APIs and integrations](#apis-and-integrations) | [FastAPI authentication](#fastapi-authentication) | Argon2 password hashing and bearer-token login | [`fastapi-authentication/`](./fastapi-authentication) |
| [APIs and integrations](#apis-and-integrations) | [Webhooks](#webhooks) | An order notification system with FastAPI webhooks | [`webhooks/`](./webhooks) |
| [APIs and integrations](#apis-and-integrations) | [GitHub sync](#github-sync) | A GitHub dashboard: React client, FastAPI server, and a Kafka pipeline | [`github-sync/`](./github-sync) |
| [Deployment and MLOps](#deployment-and-mlops) | [AWS EC2 with FastAPI](#aws-ec2-with-fastapi) | Deploy a FastAPI bookstore to EC2 behind NGINX, or to Lambda | [`aws-ec2-fastapi/`](./aws-ec2-fastapi) |
| [Deployment and MLOps](#deployment-and-mlops) | [ML pipeline on GKE](#ml-pipeline-on-gke) | Train, serve with Flask, and deploy to GKE with GitHub Actions | [`mlops-github-actions-gke/`](./mlops-github-actions-gke) |
| [Deployment and MLOps](#deployment-and-mlops) | [RAG on Kubernetes](#rag-on-kubernetes) | A RAG API on Kubernetes with Prometheus monitoring | [`rag-on-kubernetes/`](./rag-on-kubernetes) |
| [Model training](#model-training) | [Hugging Face fine-tuning](#hugging-face-fine-tuning) | Fine-tune Qwen3-0.6B for ticket routing and compare metrics | [`huggingface-finetuning/`](./huggingface-finetuning) |

## Prerequisites at a glance

What each module needs before you run it. Put keys in a `.env` in the module's folder; never commit it. Most Python modules use [uv](https://docs.astral.sh/uv/) and Python 3.13 or newer; the TypeScript modules need a current Node.js LTS.

| Module | Keys and accounts | Services and tools |
| :--- | :--- | :--- |
| [OpenAI Agents SDK in TypeScript](#openai-agents-sdk-in-typescript) | `OPENAI_API_KEY` | Node.js LTS |
| [OpenAI Agents SDK](#openai-agents-sdk) | `OPENAI_API_KEY` | Python 3 |
| [LangGraph](#langgraph) | `OPENAI_API_KEY` | Python 3 |
| [MCP crash course](#mcp-crash-course) | `OPENAI_API_KEY` (lesson 4) | Python 3, Docker (lesson 6) |
| [Redis agent memory](#redis-agent-memory) | `OPENAI_API_KEY`, `REDIS_URI` | Redis |
| [Knowledge graph](#knowledge-graph) | `OPENAI_API_KEY` | Neo4j (quickstart) |
| [Agentic RAG with Redis](#agentic-rag-with-redis) | `OPENAI_API_KEY`, Redis URL | Redis Stack, Python 3.13+ |
| [Official prompting guides](#official-prompting-guides) | — | A PDF reader |
| [Context engineering](#context-engineering) | — | Claude Code |
| [ElevenLabs voice agent](#elevenlabs-voice-agent) | `ELEVENLABS_API_KEY`, `ELEVENLABS_AGENT_ID` | Microphone, PortAudio |
| [AI code detector](#ai-code-detector) | `ANTHROPIC_API_KEY`, `DATABASE_URL` | Node.js LTS, PostgreSQL |
| [FastAPI authentication](#fastapi-authentication) | Database connection string | Python 3.13+ |
| [Webhooks](#webhooks) | — | Python 3 |
| [GitHub sync](#github-sync) | `GITHUB_TOKEN`, optional `VITE_GITHUB_*` | Docker (Kafka), Python 3.13+, Node.js or Bun |
| [AWS EC2 with FastAPI](#aws-ec2-with-fastapi) | AWS account | An EC2 instance |
| [ML pipeline on GKE](#ml-pipeline-on-gke) | GCP service account (CI secrets) | Docker, GKE, a dataset CSV |
| [RAG on Kubernetes](#rag-on-kubernetes) | `OPENAI_API_KEY` | Docker, Minikube or a cluster |
| [Hugging Face fine-tuning](#hugging-face-fine-tuning) | Hugging Face token | Jupyter, a GPU or Apple Silicon |

## Learning paths

Suggested routes through the repo. Skip anything you already know.

| Goal | Path |
| :--- | :--- |
| Build your first agent | [OpenAI Agents SDK](#openai-agents-sdk) → [LangGraph](#langgraph) → [MCP crash course](#mcp-crash-course) |
| Give agents memory and knowledge | [Redis agent memory](#redis-agent-memory) → [Agentic RAG with Redis](#agentic-rag-with-redis) → [Knowledge graph](#knowledge-graph) |
| Ship an AI service | [FastAPI authentication](#fastapi-authentication) → [AWS EC2 with FastAPI](#aws-ec2-with-fastapi) → [ML pipeline on GKE](#ml-pipeline-on-gke) → [RAG on Kubernetes](#rag-on-kubernetes) |
| Prompt better | [Official prompting guides](#official-prompting-guides) → [Context engineering](#context-engineering) |
| Build a complete app | [Webhooks](#webhooks) → [ElevenLabs voice agent](#elevenlabs-voice-agent) → [AI code detector](#ai-code-detector) → [GitHub sync](#github-sync) |
| Train a model | [Hugging Face fine-tuning](#hugging-face-fine-tuning) |

---

## Agents

Build agents that reason, call tools, and hand off work. Two SDKs and one graph framework, from a hello-world agent to multi-agent routing.

| Module | Level | Type |
| :--- | :--- | :--- |
| [OpenAI Agents SDK in TypeScript](#openai-agents-sdk-in-typescript) | 🟢 Beginner | `Tutorial` |
| [OpenAI Agents SDK](#openai-agents-sdk) | 🟡 Intermediate | `Tutorial` |
| [LangGraph](#langgraph) | 🟡 Intermediate | `Tutorial` |

**Where to start:** **OpenAI Agents SDK** (Python) or its TypeScript twin first, then **LangGraph** for explicit, stateful control flow.

### OpenAI Agents SDK in TypeScript

**Level:** 🟢 Beginner · **Type:** `Tutorial` · **Folder:** [`agent-sdk-ts/`](./agent-sdk-ts)

The OpenAI Agents SDK from TypeScript. Three short scripts, each one idea: your first agent, one agent used as a tool by another, and instructions that change at run time.

📘 **[Full guide: `agent-sdk-ts/README.md`](./agent-sdk-ts/README.md)**

### OpenAI Agents SDK

**Level:** 🟡 Intermediate · **Type:** `Tutorial` · **Folder:** [`openai-agents/`](./openai-agents)

The OpenAI Agents SDK in Python, from first agent to multi-agent routing: guardrails, graph visualization, a manager agent, and router and triage patterns.

📘 **[Full guide: `openai-agents/README.md`](./openai-agents/README.md)**

### LangGraph

**Level:** 🟡 Intermediate · **Type:** `Tutorial` · **Folder:** [`langgraph/`](./langgraph)

Stateful agents as explicit graphs. Each folder adds one idea: a basic graph, a tool-calling chatbot, ReAct, RAG, memory, a drafting agent, and the workflow patterns from Anthropic's agent guide.

📘 **[Full guide: `langgraph/README.md`](./langgraph/README.md)**

---

## Model Context Protocol (MCP)

MCP is the standard way to give models tools and data. One seven-lesson course, from concepts to Docker and lifecycle management.

| Module | Level | Type |
| :--- | :--- | :--- |
| [MCP crash course](#mcp-crash-course) | 🟡 Intermediate | `Course` |

**Where to start:** Read lessons 1 and 2 for the ideas, then run lessons 3 to 7 in order.

### MCP crash course

**Level:** 🟡 Intermediate · **Type:** `Course` · **Folder:** [`mcp-crash-course/`](./mcp-crash-course)

The Model Context Protocol (MCP) gives LLMs a standard way to connect to external data sources and tools. This seven-lesson course takes Python developers from the core concepts to servers and clients that use prompts, resources, and tools.

| Lesson | What you learn |
| :--- | :--- |
| 1. [Introduction and context](./mcp-crash-course/README.md#1-introduction-and-context) | What MCP is (a standard, not a new technology) and who this course is for |
| 2. [Understanding MCP](./mcp-crash-course/README.md#2-understanding-mcp) | Hosts, clients, servers, the three primitives, stdio vs SSE |
| 3. [Simple server setup](./mcp-crash-course/README.md#3-simple-server-setup-with-the-python-sdk) | A first FastMCP server, the Inspector, stdio and SSE clients |
| 4. [OpenAI integration](./mcp-crash-course/README.md#4-openai-integration) | OpenAI calling MCP tools over a knowledge base |
| 5. [MCP vs function calling](./mcp-crash-course/README.md#5-mcp-vs-function-calling) | When MCP pays off and when plain function calling wins |
| 6. [Running with Docker](./mcp-crash-course/README.md#6-running-with-docker) | An SSE server in a container |
| 7. [Lifecycle management](./mcp-crash-course/README.md#7-lifecycle-management) | Initialization, operation, termination, and the lifespan object |

📘 **[Full course: `mcp-crash-course/README.md`](./mcp-crash-course/README.md)**

---

## Memory, retrieval, and RAG

Give agents memory and ground answers in your data: conversational memory, knowledge graphs, and agentic RAG.

| Module | Level | Type |
| :--- | :--- | :--- |
| [Redis agent memory](#redis-agent-memory) | 🟡 Intermediate | `Tutorial` |
| [Knowledge graph](#knowledge-graph) | 🟡 Intermediate | `Tutorial` |
| [Agentic RAG with Redis](#agentic-rag-with-redis) | 🔴 Advanced | `Project` |

**Where to start:** New to Redis? Start with **Redis agent memory**. For retrieval, go to **Agentic RAG with Redis** or **Knowledge graph**. A production RAG deploy lives in [Deployment and MLOps](#rag-on-kubernetes).

### Redis agent memory

**Level:** 🟡 Intermediate · **Type:** `Tutorial` · **Folder:** [`redis-agent-memory/`](./redis-agent-memory)

Two LangGraph agents that remember. One keeps the current conversation in Redis so a thread survives restarts; the other stores facts across threads and recalls them in later sessions.

📘 **[Full guide: `redis-agent-memory/README.md`](./redis-agent-memory/README.md)**

### Knowledge graph

**Level:** 🟡 Intermediate · **Type:** `Tutorial` · **Folder:** [`knowledge-graph/`](./knowledge-graph)

Turn text into entities and relations, then query the graph instead of searching chunks. This module pairs an LLM graph extractor with a Neo4j quickstart. Stack: LangChain, OpenAI, Neo4j, PyVis.

📘 **[Full guide: `knowledge-graph/README.md`](./knowledge-graph/README.md)**

### Agentic RAG with Redis

**Level:** 🔴 Advanced · **Type:** `Project` · **Folder:** [`agentic-rag-redis/`](./agentic-rag-redis)

An agentic RAG pipeline built as a LangGraph graph on a Redis vector store, with query rewriting and relevance grading. The sample question asks what Lilian Weng wrote about the types of agent memory.

📘 **[Full guide: `agentic-rag-redis/README.md`](./agentic-rag-redis/README.md)**

---

## Prompting and context engineering

What to tell the model, and how to package it. Official prompting guides from 15 providers, plus a context-engineering workflow for AI coding assistants.

| Module | Level | Type |
| :--- | :--- | :--- |
| [Official prompting guides](#official-prompting-guides) | 🟢 Beginner | `Reference` |
| [Context engineering](#context-engineering) | 🟡 Intermediate | `Reference` |

**Where to start:** Look up your model's provider in **Official prompting guides**. Use **Context engineering** when you drive a coding agent through a whole feature.

### Official prompting guides

**Level:** 🟢 Beginner · **Type:** `Reference` · **Folder:** [`ai-dev-prompts/`](./ai-dev-prompts)

A curated index of prompting guides published **by the model providers themselves**. No third-party blogs, no "ultimate prompt" threads. If a provider ships a model-specific guide, it is listed next to the general one, because advice changes between model generations.

Every guide that is a public web page also has an offline PDF copy in `ai-dev-prompts/<provider>/`, captured in October 2026. The links are the source of truth; the PDFs are snapshots and will go stale as providers update their docs.

Providers: [Anthropic](#anthropic-claude) · [OpenAI](#openai-gpt-o-series-codex) · [Google](#google-gemini-gemma) · [Meta](#meta-llama) · [Mistral](#mistral) · [Cohere](#cohere-command) · [xAI](#xai-grok) · [DeepSeek](#deepseek) · [Qwen](#alibaba-qwen) · [Kimi](#moonshot-kimi) · [Amazon](#amazon-nova-bedrock) · [Microsoft](#microsoft-azure-openai) · [IBM](#ibm-granite) · [AI21](#ai21-jamba) · [Perplexity](#perplexity-sonar)

#### Anthropic (Claude)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) | Where to start, when prompting is (and isn't) the fix | [PDF](./ai-dev-prompts/anthropic/Claude%20Prompt%20Engineering%20Overview.pdf) |
| [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | The living reference: clarity, examples, XML tags, roles, thinking, long context, agents | [PDF](./ai-dev-prompts/anthropic/Claude%20Prompting%20Best%20Practices.pdf) |
| [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) | Model-specific notes for Opus 5.5 | [PDF](./ai-dev-prompts/anthropic/Prompting%20Claude%20Opus%205.5.pdf) |
| [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5) | Model-specific notes for Sonnet 5.5 | [PDF](./ai-dev-prompts/anthropic/Prompting%20Claude%20Sonnet%205.5.pdf) |
| [Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5) | Model-specific notes for Haiku 5.5 | [PDF](./ai-dev-prompts/anthropic/Prompting%20Claude%20Haiku%205.5.pdf) |
| [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1) | Model-specific notes for Fable 5.1 | [PDF](./ai-dev-prompts/anthropic/Prompting%20Claude%20Fable%205.1.pdf) |
| [Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) | Prompting and budgeting reasoning | [PDF](./ai-dev-prompts/anthropic/Claude%20Extended%20Thinking.pdf) |
| [System prompt release notes](https://platform.claude.com/docs/en/release-notes/system-prompts/overview) | Anthropic's own published claude.ai system prompts | — |
| [Interactive prompt engineering tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | 9-chapter hands-on course (Jupyter) | — |
| [Anthropic courses](https://github.com/anthropics/courses) | API fundamentals, real-world prompting, prompt evals, tool use | — |
| [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Context as a finite resource for agents | [PDF](./ai-dev-prompts/anthropic/Effective%20Context%20Engineering%20for%20AI%20Agents.pdf) |
| [Writing tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Tool descriptions as prompts | [PDF](./ai-dev-prompts/anthropic/Writing%20Tools%20for%20Agents.pdf) |
| [Claude Code best practices](https://www.anthropic.com/engineering/claude-code-best-practices) | Prompting an agentic coding tool | [PDF](./ai-dev-prompts/anthropic/Claude%20Code%20Best%20Practices.pdf) |

#### OpenAI (GPT, o-series, Codex)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Prompting](https://developers.openai.com/api/docs/guides/prompting) | Current general guide: messages, roles, reusable prompts | [PDF](./ai-dev-prompts/openai/OpenAI%20Prompting.pdf) |
| [Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering) | Core strategies and message formatting | [PDF](./ai-dev-prompts/openai/OpenAI%20Prompt%20Engineering.pdf) |
| [Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model/gpt-6-astra) | Latest model family, with a prompting best practices section | [PDF](./ai-dev-prompts/openai/Using%20GPT-6.pdf) |
| [Reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices) | How to prompt reasoning models differently from chat models | [PDF](./ai-dev-prompts/openai/OpenAI%20Reasoning%20Best%20Practices.pdf) |
| [GPT-5.2 prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5-2_prompting_guide) | `reasoning_effort`, verbosity, agentic scaffolding | [PDF](./ai-dev-prompts/openai/GPT-5.2%20Prompting%20Guide.pdf) |
| [GPT-5.1 prompting guide](https://cookbook.openai.com/examples/gpt-5/gpt-5-1_prompting_guide) | Personality, steerability, `none` reasoning mode | [PDF](./ai-dev-prompts/openai/GPT-5.1%20Prompting%20Guide.pdf) |
| [GPT-5 prompting guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide) | Agentic eagerness, tool preambles, coding | [PDF](./ai-dev-prompts/openai/GPT-5%20Prompting%20Guide.pdf) |
| [GPT-4.1 prompting guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide) | Literal instruction following, long context, agent prompts | [PDF](./ai-dev-prompts/openai/GPT-4.1%20Prompting%20Guide.pdf) |
| [o3 / o4-mini prompting guide](https://developers.openai.com/cookbook/examples/o-series/o3o4-mini_prompting_guide) | Function calling with reasoning models | [PDF](./ai-dev-prompts/openai/o3%20and%20o4-mini%20Prompting%20Guide.pdf) |
| [Codex prompting guide (cookbook)](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide) | Prompting Codex models for coding agents | [PDF](./ai-dev-prompts/openai/Codex%20Prompting%20Guide.pdf) |
| [Prompting Codex](https://developers.openai.com/codex/prompting) | Writing good tasks for the Codex agent | [PDF](./ai-dev-prompts/openai/Prompting%20Codex.pdf) |
| [Prompt optimization cookbook](https://cookbook.openai.com/examples/gpt-5/prompt-optimization-cookbook) | Using the prompt optimizer to fix contradictions and ambiguity | [PDF](./ai-dev-prompts/openai/Prompt%20Optimization%20Cookbook.pdf) |
| [Prompting Realtime models](https://developers.openai.com/api/docs/guides/voice-prompting) | Voice agents: tone, pacing, turn-taking | [PDF](./ai-dev-prompts/openai/Prompting%20Realtime%20Models.pdf) |
| [Realtime prompting guide (cookbook)](https://cookbook.openai.com/examples/realtime_prompting_guide) | Worked voice-agent prompt examples | [PDF](./ai-dev-prompts/openai/Realtime%20Prompting%20Guide.pdf) |
| [Prompting GPT-Live](https://developers.openai.com/api/docs/guides/live-prompting) | Live speech model prompting | [PDF](./ai-dev-prompts/openai/Prompting%20GPT-Live.pdf) |
| [Image prompting](https://developers.openai.com/api/docs/guides/image-prompting) | Prompting image generation and editing | [PDF](./ai-dev-prompts/openai/OpenAI%20Image%20Prompting.pdf) |
| [Image gen models prompting guide](https://cookbook.openai.com/examples/multimodal/image-gen-models-prompting-guide) | Worked image prompt examples | [PDF](./ai-dev-prompts/openai/Image%20Gen%20Models%20Prompting%20Guide.pdf) |
| [Sora 2 prompting guide](https://cookbook.openai.com/examples/sora/sora2_prompting_guide) | Video: shots, camera, timing, style | [PDF](./ai-dev-prompts/openai/Sora%202%20Prompting%20Guide.pdf) |
| [A practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) | Agent instructions, tools, guardrails | [PDF](./ai-dev-prompts/openai/A%20Practical%20Guide%20to%20Building%20Agents.pdf) |

#### Google (Gemini, Gemma)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Prompt design strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies) | Core Gemini API prompting guide | [PDF](./ai-dev-prompts/google/Gemini%20Prompt%20Design%20Strategies.pdf) |
| [Gemini 3 developer guide](https://ai.google.dev/gemini-api/docs/gemini-3) | Gemini 3 prompting changes: temperature, thinking level, shorter prompts | [PDF](./ai-dev-prompts/google/Gemini%203%20Developer%20Guide.pdf) |
| [What's new in Gemini 3.5 Flash](https://ai.google.dev/gemini-api/docs/generate-content/whats-new-gemini-3.5) | Migration and prompting notes for 3.5 | [PDF](./ai-dev-prompts/google/Whats%20New%20in%20Gemini%203.5%20Flash.pdf) |
| [File prompting strategies](https://ai.google.dev/gemini-api/docs/file-prompting-strategies) | Prompting with images, video, audio, PDFs | [PDF](./ai-dev-prompts/google/Gemini%20File%20Prompting%20Strategies.pdf) |
| [Image generation (Nano Banana)](https://ai.google.dev/gemini-api/docs/image-generation) | Image prompts and editing | [PDF](./ai-dev-prompts/google/Gemini%20Image%20Generation.pdf) |
| [Video generation (Veo 3.1)](https://ai.google.dev/gemini-api/docs/veo) | Veo 3.1 usage and prompt guide | [PDF](./ai-dev-prompts/google/Veo%203.1%20Video%20Generation%20and%20Prompt%20Guide.pdf) |
| [Lyria prompt guide](https://ai.google.dev/gemini-api/docs/lyria-prompt-guide) | Music generation prompting | [PDF](./ai-dev-prompts/google/Lyria%20Prompt%20Guide.pdf) |
| [Introduction to prompting (Google Cloud)](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design) | Enterprise prompting docs and strategies | [PDF](./ai-dev-prompts/google/Google%20Cloud%20Introduction%20to%20Prompting.pdf) |
| [Gemma prompt structure](https://ai.google.dev/gemma/docs/core/prompt-structure) | Gemma chat template and formatting | [PDF](./ai-dev-prompts/google/Gemma%20Prompt%20Structure.pdf) |
| [Gemini for Workspace prompt guide](https://workspace.google.com/learning/content/gemini-prompt-guide) | Prompting Gemini in Docs, Gmail, Sheets | — |
| [Prompt engineering whitepaper](https://www.kaggle.com/whitepaper-prompt-engineering) | Google's 68-page model-agnostic whitepaper | [PDF](./ai-dev-prompts/google/Prompt%20Engineering%20Whitepaper.pdf) |

#### Meta (Llama)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Prompt engineering](https://www.llama.com/docs/how-to-guides/prompting/) | Official Llama prompting how-to | [PDF](./ai-dev-prompts/meta/Llama%20Prompt%20Engineering.pdf) |
| [Model cards and prompt formats](https://www.llama.com/docs/model-cards-and-prompt-formats/) | Special tokens and chat templates per Llama version | [PDF](./ai-dev-prompts/meta/Llama%20Model%20Cards%20and%20Prompt%20Formats.pdf) |

#### Mistral

| Guide | Covers | Offline |
| --- | --- | --- |
| [Prompting capabilities](https://docs.mistral.ai/guides/prompting_capabilities) | System vs user prompts, Markdown/XML structure, few-shot, worked examples | [PDF](./ai-dev-prompts/mistral/Mistral%20Prompting%20Capabilities.pdf) |

#### Cohere (Command)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Crafting effective prompts](https://docs.cohere.com/docs/crafting-effective-prompts) | General Command prompting | [PDF](./ai-dev-prompts/cohere/Cohere%20Crafting%20Effective%20Prompts.pdf) |
| [Prompting Command R / R+](https://docs.cohere.com/docs/prompting-command-r) | Model-specific template, RAG and tool-use prompts | [PDF](./ai-dev-prompts/cohere/Prompting%20Command%20R.pdf) |

#### xAI (Grok)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Speech-to-speech prompting guide](https://docs.x.ai/developers/model-capabilities/audio/speech-to-speech/prompting-guide) | Prompting Grok voice agents | [PDF](./ai-dev-prompts/xai/Grok%20Speech-to-Speech%20Prompting%20Guide.pdf) |

xAI has no general text prompting guide right now. See the [docs home](https://docs.x.ai/docs).

#### DeepSeek

| Guide | Covers | Offline |
| --- | --- | --- |
| [DeepSeek-R1 usage recommendations](https://github.com/deepseek-ai/DeepSeek-R1#usage-recommendations) | Temperature, no few-shot, math directive, forcing `<think>` | [PDF](./ai-dev-prompts/deepseek/DeepSeek-R1%20Usage%20Recommendations.pdf) |
| [Thinking mode guide](https://api-docs.deepseek.com/guides/thinking_mode) | Using thinking mode via API | [PDF](./ai-dev-prompts/deepseek/DeepSeek%20Thinking%20Mode%20Guide.pdf) |
| [Prompt library](https://api-docs.deepseek.com/prompt-library/) | Official example prompts by task | — |

#### Alibaba (Qwen)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Qwen documentation](https://qwen.readthedocs.io/en/latest/) | Chat templates, thinking mode, function calling | — |

#### Moonshot (Kimi)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Best practices for prompts](https://platform.kimi.ai/docs/guide/prompt-best-practice) | Official Kimi prompting guide | [PDF](./ai-dev-prompts/moonshot/Kimi%20Prompt%20Best%20Practices.pdf) |

#### Amazon (Nova, Bedrock)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Nova 2 prompt engineering guide](https://docs.aws.amazon.com/nova/latest/nova2-userguide/prompt-engineering-guide.html) | Current Nova generation | [PDF](./ai-dev-prompts/amazon/Amazon%20Nova%202%20Prompt%20Engineering%20Guide.pdf) |
| [Nova (v1) prompting best practices](https://docs.aws.amazon.com/nova/latest/userguide/prompting.html) | Text, vision, image/video gen, speech | [PDF](./ai-dev-prompts/amazon/Amazon%20Nova%20Prompting%20Best%20Practices.pdf) |
| [Bedrock prompt engineering concepts](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-engineering-guidelines.html) | Hub linking to each Bedrock model's guide | [PDF](./ai-dev-prompts/amazon/Bedrock%20Prompt%20Engineering%20Concepts.pdf) |

#### Microsoft (Azure OpenAI)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/prompt-engineering) | System messages, few-shot, grounding on Azure OpenAI | [PDF](./ai-dev-prompts/microsoft/Azure%20OpenAI%20Prompt%20Engineering%20Techniques.pdf) |

#### IBM (Granite)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Granite prompt engineering guide](https://www.ibm.com/granite/docs/use-cases/prompt-engineering) | Prompt templates and techniques for Granite | [PDF](./ai-dev-prompts/ibm/Granite%20Prompt%20Engineering%20Guide.pdf) |

#### AI21 (Jamba)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Prompt engineering for Jamba](https://docs.ai21.com/docs/prompt-engineering) | Jamba-specific prompting | [PDF](./ai-dev-prompts/ai21/Jamba%20Prompt%20Engineering.pdf) |

#### Perplexity (Sonar)

| Guide | Covers | Offline |
| --- | --- | --- |
| [Prompt guide](https://docs.perplexity.ai/docs/agent-api/prompt-guide) | Prompting search-grounded models | [PDF](./ai-dev-prompts/perplexity/Perplexity%20Prompt%20Guide.pdf) |

#### About the PDFs

- Web pages were printed with headless Chrome, and large images were downscaled to keep the folder small.
- The Amazon Nova guides are split across many pages online, so each PDF merges a whole section into one file.
- `openai/GPT-4.1 Prompting Guide.pdf` and `openai/A Practical Guide to Building Agents.pdf` are OpenAI's own PDFs, and `google/Prompt Engineering Whitepaper.pdf` is Google's.
- No PDFs for GitHub repos, docs home pages, or the Gemini for Workspace guide (it is behind a sign-up form).
- To add a guide: it must be published by the model's provider. Put the newest model-specific guide first in its provider's table, and add a PDF snapshot to the provider's folder.

### Context engineering

**Level:** 🟡 Intermediate · **Type:** `Reference` · **Folder:** [`context-engineering/`](./context-engineering)

A template for context engineering: giving AI coding assistants all the information they need to finish a job end to end. You describe a feature, generate a PRP (Product Requirements Prompt) with full context and validation gates, then let the assistant execute it. The folder is meant to be copied out as the start of your own project.

**Quick start (in Claude Code)**

1. Edit `CLAUDE.md` with your project rules.
2. Put relevant code examples in `examples/`.
3. Describe the feature in `INITIAL.md` (see `INITIAL_EXAMPLE.md`).
4. `/generate-prp INITIAL.md`
5. `/execute-prp PRPs/your-feature-name.md`

**Depends on:** Claude Code. The slash commands live in `context-engineering/.claude/commands/`.

📘 **[Full guide: `context-engineering/README.md`](./context-engineering/README.md)**: template structure, writing `INITIAL.md`, the PRP workflow, using examples, and best practices.

---

## AI applications

Complete apps where the model is the product: a live voice agent and an AI-generated-code detector.

| Module | Level | Type |
| :--- | :--- | :--- |
| [ElevenLabs voice agent](#elevenlabs-voice-agent) | 🟡 Intermediate | `Project` |
| [AI code detector](#ai-code-detector) | 🔴 Advanced | `Project` |

**Where to start:** Pick the one closest to what you want to ship. Both run end to end.

### ElevenLabs voice agent

**Level:** 🟡 Intermediate · **Type:** `Project` · **Folder:** [`elevenlabs-voice-agent/`](./elevenlabs-voice-agent)

A live voice agent for a clinic front desk. You speak, the agent answers, and it calls client-side tools to look up patient records and book appointments.

📘 **[Full guide: `elevenlabs-voice-agent/README.md`](./elevenlabs-voice-agent/README.md)**

### AI code detector

**Level:** 🔴 Advanced · **Type:** `Project` · **Folder:** [`ai-code-detector/`](./ai-code-detector)

An Express and TypeScript backend that asks Claude whether a piece of code looks AI-generated. It also takes GitHub webhooks, so it can check pull requests and commits as they arrive.

📘 **[Full guide: `ai-code-detector/README.md`](./ai-code-detector/README.md)**

---

## APIs and integrations

The backend plumbing around AI apps: authentication, webhooks, and event streaming with Kafka.

| Module | Level | Type |
| :--- | :--- | :--- |
| [FastAPI authentication](#fastapi-authentication) | 🟢 Beginner | `Project` |
| [Webhooks](#webhooks) | 🟢 Beginner | `Tutorial` |
| [GitHub sync](#github-sync) | 🔴 Advanced | `Project` |

**Where to start:** **FastAPI authentication** and **Webhooks** are small and self-contained. **GitHub sync** combines a React client, a FastAPI server, and Kafka.

### FastAPI authentication

**Level:** 🟢 Beginner · **Type:** `Project` · **Folder:** [`fastapi-authentication/`](./fastapi-authentication)

A small FastAPI service with real password handling. Passwords hash with Argon2. Users log in and get a bearer token.

📘 **[Full guide: `fastapi-authentication/README.md`](./fastapi-authentication/README.md)**

### Webhooks

**Level:** 🟢 Beginner · **Type:** `Tutorial` · **Folder:** [`webhooks/`](./webhooks)

A practical webhook example with FastAPI: an order notification system. When a customer places an order, the system notifies an inventory system (to update stock), an email service (to send confirmation), and an analytics service (to track metrics).

📘 **[Full guide: `webhooks/README.md`](./webhooks/README.md)**

### GitHub sync

**Level:** 🔴 Advanced · **Type:** `Project` · **Folder:** [`github-sync/`](./github-sync)

A full-stack GitHub dashboard. A React client signs you in and shows commits, pull requests, repositories, and organizations. A FastAPI server talks to the GitHub API. Kafka carries events between producer and consumer.

| Part | Path | Stack |
| :--- | :--- | :--- |
| Client | `github-sync/client/` | React, Vite, Bun or npm |
| API server | `github-sync/server/Github/` | FastAPI, httpx, Pydantic |
| Event pipeline | `github-sync/server/Kafka/` | Kafka and ZooKeeper in Docker |

📘 **[Full guide: `github-sync/README.md`](./github-sync/README.md)**: API endpoints, client sign-in (OAuth or token), project structure, and Kafka notes.

---

## Deployment and MLOps

Get models and APIs into production: a VM, a CI/CD pipeline to Kubernetes, and a monitored RAG service.

| Module | Level | Type |
| :--- | :--- | :--- |
| [AWS EC2 with FastAPI](#aws-ec2-with-fastapi) | 🟢 Beginner | `Tutorial` |
| [ML pipeline on GKE](#ml-pipeline-on-gke) | 🟡 Intermediate | `Project` |
| [RAG on Kubernetes](#rag-on-kubernetes) | 🔴 Advanced | `Project` |

**Where to start:** **AWS EC2 with FastAPI** is the simplest deploy. **ML pipeline on GKE** adds CI/CD. **RAG on Kubernetes** adds monitoring.

### AWS EC2 with FastAPI

**Level:** 🟢 Beginner · **Type:** `Tutorial` · **Folder:** [`aws-ec2-fastapi/`](./aws-ec2-fastapi)

A simple FastAPI app that pretends to be a bookstore (`main.py`, `books.json`), and how to deploy it to AWS EC2 behind NGINX, or to AWS Lambda. More commands are in [`aws-ec2-fastapi/Run_Commands.md`](./aws-ec2-fastapi/Run_Commands.md).

📘 **[Full guide: `aws-ec2-fastapi/README.md`](./aws-ec2-fastapi/README.md)**

### ML pipeline on GKE

**Level:** 🟡 Intermediate · **Type:** `Project` · **Folder:** [`mlops-github-actions-gke/`](./mlops-github-actions-gke)

A complete ML delivery loop. Data processing and training run as a pipeline. A Flask app serves the model. Docker packages it. A GitHub Actions workflow deploys it to Google Kubernetes Engine on every push to `main`.

📘 **[Full guide: `mlops-github-actions-gke/README.md`](./mlops-github-actions-gke/README.md)**

### RAG on Kubernetes

**Level:** 🔴 Advanced · **Type:** `Project` · **Folder:** [`rag-on-kubernetes/`](./rag-on-kubernetes)

A RAG API packaged for Kubernetes, with Prometheus monitoring and a faster retrieval pipeline (hybrid dense and BM25 search, recursive chunking, an embedding cache). Runs locally with Docker or on Minikube.

📘 **[Full guide: `rag-on-kubernetes/README.md`](./rag-on-kubernetes/README.md)**

---

## Model training

Fine-tune an open model and measure the gain with before-and-after metrics.

| Module | Level | Type |
| :--- | :--- | :--- |
| [Hugging Face fine-tuning](#hugging-face-fine-tuning) | 🔴 Advanced | `Tutorial` |

**Where to start:** Open the notebook and run it top to bottom. A GPU helps.

### Hugging Face fine-tuning

**Level:** 🔴 Advanced · **Type:** `Tutorial` · **Folder:** [`huggingface-finetuning/`](./huggingface-finetuning)

Train and evaluate open-source models. The notebook fine-tunes a small LLM and measures the gain, so you see before and after numbers instead of a guess. Stack: Transformers, PEFT, Datasets, PyTorch.

| Path | What it does |
| :--- | :--- |
| [`hf-model-trainer-skill.ipynb`](./huggingface-finetuning/hf-model-trainer-skill.ipynb) | Fine-tunes `Qwen/Qwen3-0.6B` to route customer support tickets. Trains on the Bitext customer support dataset and compares routing metrics before and after, with plots |

**Run**

1. Open the notebook in Jupyter, VS Code, or Colab.
2. Run the setup cell. It installs the dependencies with `uv`, or with `pip` if you prefer.
3. Run the cells in order. A GPU speeds up training. Apple Silicon (MPS) also works.

**Depends on**

- A Hugging Face account and token for dataset and model downloads.

---

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) first.

1. Open a **Module proposal** [issue](../../issues/new/choose) for a new module.
2. Fork the repository and create a branch.
3. Improve a module, or add a new top-level folder for one.
4. Document it in this README only. Add its section under the right area with the [module section template](.github/MODULE_SECTION_TEMPLATE.md), and add rows to the [Module map](#module-map) and [Prerequisites at a glance](#prerequisites-at-a-glance). Modules don't have their own README files.
5. Open a pull request. The template lists the checks.

Report a leaked secret through [private reporting](SECURITY.md). Everyone must follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

MIT. See [LICENSE](LICENSE).

Created by Kushal Banda.

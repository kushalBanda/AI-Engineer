# LineTrace Codebase Analysis

### File Structure Summary
- Total Files: 301
- Total Directories: 109
- File Extensions: .lock: 7, .toml: 6, .md: 42, .txt: 15, .py: 129, .png: 6, .mdc: 4, .pdf: 11, .csv: 5, .json: 15, .js: 10, .yaml: 5, .css: 7, .html: 3, .xml: 1, .pkl: 5, .log: 1, .pem: 1, .yml: 1, .jsx: 7, .ts: 10

### Directory Tree
```
  ├── Langgraph
   │  ├── Basics
   │  │  ├── requirements.txt
   │  │  └── Basic.py
   │  ├── Chatbot
   │  │  ├── requirements.txt
   │  │  ├── Tools.py
   │  │  └── Graph.png
   │  ├── Agent
   │  │  ├── ReAct_Bot.py
   │  │  ├── Drafter.py
   │  │  ├── RAG.py
   │  │  ├── Memory_Bot.py
   │  │  └── Agent_Bot.py
   │  ├── Subgraphs
   │  │  ├── parent_graph.png
   │  │  ├── Subgraphs.py
   │  │  └── subgraph.png
   │  ├── Advanced AI Agent
   │  │  ├── uv.lock
   │  │  ├── pyproject.toml
   │  │  ├── README.md
   │  │  └── main.py
   │  └── Workflows + Agents
   │    ├── PromptChaining.py
   │    ├── Augment.py
   │    └── Parallelization.py
  ├── Prompts & PRD
   │  ├── AI-Prompts
   │  │  ├── create-prd.mdc
   │  │  ├── generate-tasks.mdc
   │  │  ├── README.md
   │  │  ├── coding-instructions.mdc
   │  │  └── process-task-list.mdc
   │  ├── Context Engineering
   │  │  ├── INITIAL_EXAMPLE.md
   │  │  ├── INITIAL.md
   │  │  ├── README.md
   │  │  ├── examples
   │  │  ├── PRPs
   │  │  │  ├── EXAMPLE_multi_agent_prp.md
   │  │  │  └── templates
   │  │  │    └── prp_base.md
   │  │  └── CLAUDE.md
   │  └── Prompts
   │    └── GPT-4.1 Prompting Guide.pdf
  ├── LICENSE
  ├── uv.lock
  ├── Redis
   │  ├── Memory
   │  │  ├── short_term_memory.py
   │  │  └── long_term_memory_agent.py
   │  ├── Python
   │  │  └── Redis.py
   │  ├── vectorLibrary
   │  │  ├── uv.lock
   │  │  ├── resources
   │  │  │  ├── nke-10k-2023.pdf
   │  │  │  ├── amzn-10k-2023.pdf
   │  │  │  ├── jnj-10k-2023.pdf
   │  │  │  ├── aapl-10k-2023.pdf
   │  │  │  ├── testset_15.csv
   │  │  │  ├── retrieval_basic_rag_test.csv
   │  │  │  ├── 2022-chevy-colorado-ebrochure.pdf
   │  │  │  ├── nvd-10k-2023.pdf
   │  │  │  ├── testset.csv
   │  │  │  ├── msft-10k-2023.pdf
   │  │  │  ├── propositions.json
   │  │  │  └── generation_basic_rag_test.csv
   │  │  ├── pyproject.toml
   │  │  └── src
   │  │    ├── cache
   │  │     │  ├── __init__.py
   │  │     │  └── connection.py
   │  │    ├── config
   │  │     │  ├── __init__.py
   │  │     │  ├── openai.py
   │  │     │  └── settings.py
   │  │    ├── resources
   │  │     │  └── 2501.12948.pdf
   │  │    ├── retriever.py
   │  │    ├── __init__.py
   │  │    ├── agents
   │  │     │  ├── mermaid.py
   │  │     │  ├── graph.py
   │  │     │  ├── __init__.py
   │  │     │  ├── edges.py
   │  │     │  └── nodes.py
   │  │    └── main.py
   │  └── Javascript
   │    ├── client.js
   │    ├── server.js
   │    ├── list.js
   │    └── string.js
  ├── MLOPS
   │  ├── artifacts
   │  ├── Tools
   │  │  └── Readme.md
   │  ├── DockerAI
   │  │  └── docker-genai-sample
   │  │    ├── chains.py
   │  │    ├── requirements.txt
   │  │    ├── Dockerfile
   │  │    ├── README.Docker.md
   │  │    ├── README.md
   │  │    ├── utils.py
   │  │    ├── app.py
   │  │    └── compose.yaml
   │  ├── Hotel_Price_Prediction_MLOPS
   │  │  ├── pipeline
   │  │  │  ├── training_pipeline.py
   │  │  │  └── __init__.py
   │  │  ├── LICENSE
   │  │  ├── requirements.txt
   │  │  ├── config
   │  │  │  ├── model_params.py
   │  │  │  ├── paths_config.py
   │  │  │  ├── config.yaml
   │  │  │  └── __init__.py
   │  │  ├── Dockerfile
   │  │  ├── utils
   │  │  │  ├── __init__.py
   │  │  │  └── common_functions.py
   │  │  ├── README.md
   │  │  ├── Env
   │  │  ├── application.py
   │  │  ├── setup.py
   │  │  ├── static
   │  │  │  └── style.css
   │  │  ├── Jenkinsfile
   │  │  ├── CI_CD.md
   │  │  ├── templates
   │  │  │  └── index.html
   │  │  ├── CI_CD_1.txt
   │  │  ├── custom_jenkins
   │  │  │  ├── Dockerfile
   │  │  │  └── config.xml
   │  │  └── src
   │  │    ├── data_preprocessing.py
   │  │    ├── model_training.py
   │  │    ├── data_ingestion.py
   │  │    ├── custom_exception.py
   │  │    ├── __init__.py
   │  │    └── logger.py
   │  ├── GithubActions
   │  │  ├── pipeline
   │  │  │  └── __init__.py
   │  │  ├── artifacts
   │  │  │  ├── models
   │  │  │  │  ├── confusion_matrix.png
   │  │  │  │  └── model.pkl
   │  │  │  ├── processed
   │  │  │  │  ├── y_train.pkl
   │  │  │  │  ├── X_test.pkl
   │  │  │  │  ├── y_test.pkl
   │  │  │  │  └── X_train.pkl
   │  │  │  └── raw
   │  │  │    └── data.csv
   │  │  ├── requirements.txt
   │  │  ├── able-analyst-431912-a9-a307934d5ca7.json
   │  │  ├── Dockerfile
   │  │  ├── training_pipeline.py
   │  │  ├── README.md
   │  │  ├── application.py
   │  │  ├── setup.py
   │  │  ├── logs
   │  │  │  └── log_2025-03-30.log
   │  │  ├── static
   │  │  ├── templates
   │  │  │  └── index.html
   │  │  ├── kubernetes-deployment.yaml
   │  │  └── src
   │  │    ├── model_training.py
   │  │    ├── custom_exception.py
   │  │    ├── __init__.py
   │  │    ├── logger.py
   │  │    └── data_processing.py
   │  └── Lambda_GitHubActions
   │    ├── README.md
   │    └── lambda_function.py
  ├── pyproject.toml
  ├── MCP
   │  ├── requirements.txt
   │  ├── 1-introduction-and-context
   │  │  └── README.md
   │  ├── 7-lifecycle-management
   │  │  └── README.md
   │  ├── 3-simple-server-setup
   │  │  ├── server.py
   │  │  ├── README.md
   │  │  ├── client-sse.py
   │  │  └── client-stdio.py
   │  ├── 6-run-with-docker
   │  │  ├── server.py
   │  │  ├── requirements.txt
   │  │  ├── Dockerfile
   │  │  ├── client.py
   │  │  └── README.md
   │  ├── README.md
   │  ├── 5-mcp-vs-function-calling
   │  │  ├── tools.py
   │  │  ├── README.md
   │  │  └── function-calling.py
   │  ├── 4-openai-integration
   │  │  ├── server.py
   │  │  ├── client.py
   │  │  ├── client-simple.py
   │  │  ├── README.md
   │  │  └── data
   │  │    └── kb.json
   │  └── 2-understanding-mcp
   │    └── README.md
  ├── Openai Agents
   │  ├── GPT-4.1 Prompting Guide.pdf
   │  ├── Agent
   │  │  ├── 03_Guardrails.py
   │  │  ├── 04_Manager_Agent.py
   │  │  ├── 01_Simple_Agent.py
   │  │  ├── 02_Graph_Visualization.py
   │  │  └── agent_graph.png.png
   │  ├── Agentic Patterns
   │  │  ├── Patterns
   │  │  │  └── Triage_Agent.png
   │  │  ├── config
   │  │  │  ├── config.py
   │  │  │  └── __init__.py
   │  │  ├── 1. Router Agent.py
   │  │  └── 2. Triage Agent.py
   │  ├── Agent SDK
   │  │  └── agents-sdk-intro.py
   │  └── Practical-guide-to-building-agents.pdf
  ├── KnowledgeGraph
   │  ├── Neo4j
   │  │  ├── config.py
   │  │  └── Quickstart.py
   │  ├── config.py
   │  ├── requirements.txt
   │  └── KG.py
  ├── README.md
  ├── AgentSDK-Ts
   │  ├── agentTool.js
   │  ├── Readme.md
   │  ├── package-lock.json
   │  ├── package.json
   │  ├── helloWorld.js
   │  └── dynamicInstructions.js
  ├── LineTrace.md
  ├── AWS
   │  ├── EC2-FastAPI
   │  │  ├── requirements.txt
   │  │  ├── Run_Commands.md
   │  │  ├── README.md
   │  │  ├── books.json
   │  │  ├── FastAPI Key.pem
   │  │  ├── main.py
   │  │  └── CLAUDE.md
   │  └── EC2
   │    └── FastAPI
  ├── GEMINI.md
  ├── AGENTS.md
  ├── Kubernetes
   │  ├── uv.lock
   │  ├── pyproject.toml
   │  ├── README.md
   │  ├── rag-app
   │  │  ├── app
   │  │  │  ├── config.py
   │  │  │  ├── __init__.py
   │  │  │  ├── utils
   │  │  │  │  ├── __init__.py
   │  │  │  │  └── text.py
   │  │  │  ├── api.py
   │  │  │  ├── schemas.py
   │  │  │  ├── main.py
   │  │  │  └── services
   │  │  │    ├── store.py
   │  │  │    ├── __init__.py
   │  │  │    ├── llm.py
   │  │  │    ├── embeddings.py
   │  │  │    └── retrieval.py
   │  │  ├── requirements.txt
   │  │  ├── Dockerfile
   │  │  ├── Makefile
   │  │  ├── k8s
   │  │  │  ├── deployment.yaml
   │  │  │  └── service.yaml
   │  │  ├── postman
   │  │  │  ├── postman_collection.json
   │  │  │  └── postman_environment.json
   │  │  ├── README.md
   │  │  └── data
   │  │    └── index.json
   │  └── CLAUDE.md
  ├── Webhooks
   │  ├── sender.py
   │  ├── requirements.txt
   │  ├── receiver.py
   │  ├── test.py
   │  └── README.md
  ├── GithubSync
   │  ├── server
   │  │  ├── uv.lock
   │  │  ├── chat
   │  │  │  ├── 4. Enhanced Kafka Based GitHub Sync Plan.txt
   │  │  │  ├── 1. GithubFlow.txt
   │  │  │  └── 2. Kafka Based Github Sync.txt
   │  │  ├── Auth
   │  │  │  ├── Auth.py
   │  │  │  └── __init__.py
   │  │  ├── pyproject.toml
   │  │  ├── Postman
   │  │  │  └── postman_collection.json
   │  │  ├── README.md
   │  │  ├── Github
   │  │  │  ├── __init__.py
   │  │  │  ├── README.md
   │  │  │  ├── api
   │  │  │  │  ├── routers
   │  │  │  │  │  ├── commits.py
   │  │  │  │  │  ├── organization.py
   │  │  │  │  │  ├── __init__.py
   │  │  │  │  │  ├── pull_requests.py
   │  │  │  │  │  └── repository.py
   │  │  │  │  ├── core
   │  │  │  │  │  ├── config.py
   │  │  │  │  │  ├── __init__.py
   │  │  │  │  │  └── app.py
   │  │  │  │  ├── __init__.py
   │  │  │  │  ├── utils
   │  │  │  │  │  ├── client.py
   │  │  │  │  │  ├── __init__.py
   │  │  │  │  │  └── exceptions.py
   │  │  │  │  ├── models
   │  │  │  │  │  ├── __init__.py
   │  │  │  │  │  └── schemas.py
   │  │  │  │  └── controllers
   │  │  │  │    ├── commits.py
   │  │  │  │    ├── organization.py
   │  │  │  │    ├── __init__.py
   │  │  │  │    ├── pull_requests.py
   │  │  │  │    └── repository.py
   │  │  │  └── main.py
   │  │  ├── Kafka
   │  │  │  ├── __init__.py
   │  │  │  ├── Producer.py
   │  │  │  └── Consumer.py
   │  │  ├── docker-compose.yml
   │  │  ├── controllers
   │  │  │  ├── repository_controller.py
   │  │  │  ├── user_controller.py
   │  │  │  ├── commit_controller.py
   │  │  │  ├── __init__.py
   │  │  │  └── pull_request_controller.py
   │  │  └── CLAUDE.md
   │  └── client
   │    ├── REACT_GUIDE.md
   │    ├── index.html
   │    ├── GITHUB_THEME.md
   │    ├── vite.config.js
   │    ├── bun.lock
   │    ├── README.md
   │    ├── package-lock.json
   │    ├── package.json
   │    ├── BUN_GUIDE.md
   │    └── src
   │       ├── contexts
   │        │  └── AuthContext.jsx
   │       ├── App.css
   │       ├── index.css
   │       ├── components
   │        │  ├── UserProfile.css
   │        │  ├── Login.css
   │        │  ├── Dashboard.css
   │        │  ├── OrganizationsList.jsx
   │        │  ├── Dashboard.jsx
   │        │  ├── Login.jsx
   │        │  ├── UserProfile.jsx
   │        │  └── OrganizationsList.css
   │       ├── main.jsx
   │       ├── App.jsx
   │       └── services
   │          ├── githubOAuth.js
   │          └── api.js
  ├── Authentication
   │  ├── models.py
   │  ├── uv.lock
   │  ├── database.py
   │  ├── pyproject.toml
   │  └── main.py
  └── AICodeDetector
     ├── postman
      │  └── AICodeDetector.postman_collection.json
     └── backend
        ├── package-lock.json
        ├── package.json
        └── src
           ├── app.ts
           ├── utils
            │  └── githubSignature.ts
           ├── db
            │  └── db.ts
           ├── server.ts
           ├── routes
            │  ├── detect.ts
            │  ├── github.ts
            │  └── health.ts
           └── services
              ├── github.ts
              ├── anthropic.ts
              └── health.ts
```


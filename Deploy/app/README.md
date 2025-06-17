# OpenAI Agent FastAPI Application

A simple FastAPI application that integrates with OpenAI to create an AI agent that can respond to user queries.

## Setup

### Option 1: Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key as an environment variable:
```bash
export OPENAI_API_KEY="your-openai-api-key-here"
```

3. Run the application:
```bash
python main.py
```

### Option 2: Docker

1. Build the Docker image:
```bash
docker build -t openai-agent-api .
```

2. Run the container with your OpenAI API key:
```bash
docker run -p 8000:8000 -e OPENAI_API_KEY="your-openai-api-key-here" openai-agent-api
```

**Important**: Make sure to replace `your-openai-api-key-here` with your actual OpenAI API key.

The application will start on `http://localhost:8000`

## API Endpoints

### GET /
Welcome message

### GET /health
Health check endpoint

### POST /chat
Send a query to the OpenAI agent

**Request body:**
```json
{
    "query": "Your question here",
    "model": "gpt-3.5-turbo",
    "max_tokens": 1000
}
```
*Note: `model` and `max_tokens` are optional parameters*

**Response:**
```json
{
    "response": "AI agent response",
    "model_used": "gpt-3.5-turbo"
}
```

## Example Usage

### Using curl
```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{"query": "What is the capital of France?"}'
```

### Using Python requests
```python
import requests

response = requests.post(
    "http://localhost:8000/chat",
    json={"query": "What is machine learning?"}
)
print(response.json())
```

## Interactive Documentation

Visit `http://localhost:8000/docs` for interactive API documentation powered by Swagger UI.

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)

## Troubleshooting

### Common Issues

1. **OpenAI API Key Error**: 
   - Make sure your API key is set correctly
   - Check `/health` endpoint to verify API key status
   - For Docker: Ensure you're passing the API key with `-e OPENAI_API_KEY="your-key"`

2. **httpx/OpenAI Compatibility Error**:
   - This is fixed in the current requirements.txt with compatible versions
   - If you encounter issues, rebuild your Docker image

3. **Port Issues**:
   - The application runs on port 8000 by default
   - Make sure port 8000 is available or change the port mapping

## Dependencies

- FastAPI: Web framework
- OpenAI: OpenAI API client (v1.51.0)
- Uvicorn: ASGI server
- Pydantic: Data validation
- python-dotenv: Environment variable loading
- httpx: HTTP client (v0.27.0 for compatibility) 
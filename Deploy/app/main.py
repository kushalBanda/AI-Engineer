from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI(title="OpenAI Agent API", description="Simple FastAPI application for OpenAI agents")

def get_openai_client():
    """Get OpenAI client with proper error handling"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500, 
            detail="OpenAI API key not configured. Please set the OPENAI_API_KEY environment variable."
        )
    return OpenAI(api_key=api_key)

class QueryRequest(BaseModel):
    query: str
    model: Optional[str] = "gpt-3.5-turbo"
    max_tokens: Optional[int] = 1000

class QueryResponse(BaseModel):
    response: str
    model_used: str

@app.get("/")
async def root():
    return {"message": "Welcome to OpenAI Agent API"}

@app.get("/health")
async def health_check():
    # Check if API key is configured
    api_key_status = "configured" if os.getenv("OPENAI_API_KEY") else "not configured"
    return {
        "status": "healthy",
        "openai_api_key": api_key_status
    }

@app.post("/chat", response_model=QueryResponse)
async def chat_with_agent(request: QueryRequest):
    """
    Send a query to the OpenAI agent and get a response
    """
    try:
        # Get client with error handling
        client = get_openai_client()
        
        response = client.chat.completions.create(
            model=request.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": request.query}
            ],
            max_tokens=request.max_tokens
        )
        
        return QueryResponse(
            response=response.choices[0].message.content,
            model_used=request.model
        )
    
    except HTTPException:
        # Re-raise HTTP exceptions (like missing API key)
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8090) 
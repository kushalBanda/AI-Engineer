import json
import httpx
from redis import Redis
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    app.state.redis = Redis(host="localhost", port=6379)
    app.state.http_client = httpx.AsyncClient()

@app.on_event("shutdown")
async def shutdown_event():
    await app.state.redis.close()

@app.get("/entries")
async def get_entries():
    value = app.state.redis.get("entries")
    
    if value is None:
        response = await app.state.http_client.get("https://jsonplaceholder.typicode.com/posts")
        value = response.json()
        app.state.redis.set("entries", json.dumps(value))
    else:
        value = json.loads(value)

    return value



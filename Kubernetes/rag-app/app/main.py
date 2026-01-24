from fastapi import FastAPI

from .api import router

app = FastAPI(title="rag-app")
app.include_router(router)

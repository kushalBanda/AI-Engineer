"""GitHub API application factory."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ..routers import organization, repository, commits, pull_requests


def create_app() -> FastAPI:
    """Create and configure FastAPI application.

    Returns:
        FastAPI: Configured FastAPI application
    """
    app = FastAPI(
        title="GitHub API",
        description="FastAPI wrapper for GitHub REST API",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], 
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(organization.router)
    app.include_router(repository.router)
    app.include_router(commits.router)
    app.include_router(pull_requests.router)

    @app.get("/health", tags=["Health"])
    async def health_check() -> dict:
        """Health check endpoint."""
        return {"status": "ok"}

    return app

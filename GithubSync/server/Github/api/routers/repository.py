"""Repository API router."""

from fastapi import APIRouter, Depends
from ..controllers.repository import (
    RepositoryController,
    get_repository_controller,
)
from ..models import RepositoryResponse


router = APIRouter(
    prefix="/repos",
    tags=["Repositories"],
    responses={
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
    },
)


@router.get(
    "/{owner}/{repo}",
    response_model=RepositoryResponse,
    summary="Get repository details",
    description="Get detailed information about a specific repository",
)
async def get_repository(
    owner: str,
    repo: str,
    controller: RepositoryController = Depends(get_repository_controller),
) -> RepositoryResponse:
    """Get repository details."""
    return await controller.get_repository(owner, repo)

"""Commits API router."""

from typing import List, Optional
from fastapi import APIRouter, Depends
from ..controllers.commits import (
    CommitsController,
    get_commits_controller,
)
from ..models import CommitResponse, CommitDetailResponse


router = APIRouter(
    prefix="/repos",
    tags=["Commits"],
    responses={
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
    },
)


@router.get(
    "/{owner}/{repo}/commits",
    response_model=List[CommitResponse],
    summary="List repository commits",
    description="Get list of commits in a repository",
)
async def list_commits(
    owner: str,
    repo: str,
    per_page: int = 30,
    page: int = 1,
    sha: Optional[str] = None,
    controller: CommitsController = Depends(get_commits_controller),
) -> List[CommitResponse]:
    """List commits of a repository."""
    return await controller.list_commits(owner, repo, per_page, page, sha)


@router.get(
    "/{owner}/{repo}/commits/{commit_sha}",
    response_model=CommitDetailResponse,
    summary="Get commit details",
    description="Get detailed information about a specific commit",
)
async def get_commit(
    owner: str,
    repo: str,
    commit_sha: str,
    controller: CommitsController = Depends(get_commits_controller),
) -> CommitDetailResponse:
    """Get a single commit by SHA."""
    return await controller.get_commit(owner, repo, commit_sha)

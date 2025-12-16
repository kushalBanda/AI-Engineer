"""Pull Requests API router."""

from typing import List
from fastapi import APIRouter, Depends
from ..controllers.pull_requests import (
    PullRequestsController,
    get_pull_requests_controller,
)
from ..models import PullRequestResponse, CommitResponse


router = APIRouter(
    prefix="/repos",
    tags=["Pull Requests"],
    responses={
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
    },
)


@router.get(
    "/{owner}/{repo}/pulls",
    response_model=List[PullRequestResponse],
    summary="List repository pull requests",
    description="Get list of pull requests in a repository",
)
async def list_pull_requests(
    owner: str,
    repo: str,
    state: str = "all",
    per_page: int = 30,
    page: int = 1,
    controller: PullRequestsController = Depends(get_pull_requests_controller),
) -> List[PullRequestResponse]:
    """List all pull requests for a repository."""
    return await controller.list_pull_requests(
        owner, repo, state, per_page, page
    )


@router.get(
    "/{owner}/{repo}/pulls/{pull_number}",
    response_model=PullRequestResponse,
    summary="Get pull request details",
    description="Get detailed information about a specific pull request",
)
async def get_pull_request(
    owner: str,
    repo: str,
    pull_number: int,
    controller: PullRequestsController = Depends(get_pull_requests_controller),
) -> PullRequestResponse:
    """Get a single pull request by number."""
    return await controller.get_pull_request(owner, repo, pull_number)


@router.get(
    "/{owner}/{repo}/pulls/{pull_number}/commits",
    response_model=List[CommitResponse],
    summary="List pull request commits",
    description="Get list of commits in a pull request",
)
async def list_pull_request_commits(
    owner: str,
    repo: str,
    pull_number: int,
    per_page: int = 30,
    page: int = 1,
    controller: PullRequestsController = Depends(get_pull_requests_controller),
) -> List[CommitResponse]:
    """List commits in a pull request."""
    return await controller.list_pull_request_commits(
        owner, repo, pull_number, per_page, page
    )

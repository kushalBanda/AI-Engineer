"""Pull Requests controller for GitHub API."""

from typing import List, Optional
from fastapi import Depends
from ..utils import GitHubClient
from ..models import PullRequestResponse, CommitResponse
from .organization import get_github_token


class PullRequestsController:
    """Controller for pull request operations."""

    def __init__(self, client: GitHubClient):
        """Initialize controller with GitHub client.

        Args:
            client: GitHubClient instance
        """
        self.client = client

    async def list_pull_requests(
        self,
        owner: str,
        repo: str,
        state: str = "all",
        per_page: int = 30,
        page: int = 1,
    ) -> List[PullRequestResponse]:
        """List all pull requests for a repository.

        Args:
            owner: Repository owner username
            repo: Repository name
            state: Filter by state (open, closed, all) - default: all
            per_page: Number of results per page (max 100)
            page: Page number

        Returns:
            List[PullRequestResponse]: List of pull requests
        """
        params = {
            "state": state,
            "per_page": min(per_page, 100),
            "page": page,
        }
        data = await self.client.get(
            f"/repos/{owner}/{repo}/pulls",
            params=params,
        )
        return [PullRequestResponse(**pr) for pr in data]

    async def get_pull_request(
        self,
        owner: str,
        repo: str,
        pull_number: int,
    ) -> PullRequestResponse:
        """Get a single pull request by number.

        Args:
            owner: Repository owner username
            repo: Repository name
            pull_number: Pull request number

        Returns:
            PullRequestResponse: Pull request data
        """
        data = await self.client.get(
            f"/repos/{owner}/{repo}/pulls/{pull_number}",
        )
        return PullRequestResponse(**data)

    async def list_pull_request_commits(
        self,
        owner: str,
        repo: str,
        pull_number: int,
        per_page: int = 30,
        page: int = 1,
    ) -> List[CommitResponse]:
        """List commits in a pull request.

        Args:
            owner: Repository owner username
            repo: Repository name
            pull_number: Pull request number
            per_page: Number of results per page (max 100)
            page: Page number

        Returns:
            List[CommitResponse]: List of commits
        """
        params = {"per_page": min(per_page, 100), "page": page}
        data = await self.client.get(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/commits",
            params=params,
        )
        return [CommitResponse(**commit) for commit in data]


def get_pull_requests_controller(
    token: str = Depends(get_github_token),
) -> PullRequestsController:
    """Dependency injection for PullRequestsController.

    Args:
        token: GitHub token

    Returns:
        PullRequestsController: Instance of controller
    """
    client = GitHubClient(token)
    return PullRequestsController(client)

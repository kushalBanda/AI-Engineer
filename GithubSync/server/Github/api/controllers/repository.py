"""Repository controller for GitHub API."""

from fastapi import Depends
from ..utils import GitHubClient
from ..models import RepositoryResponse
from .organization import get_github_token


class RepositoryController:
    """Controller for repository operations."""

    def __init__(self, client: GitHubClient):
        """Initialize controller with GitHub client.

        Args:
            client: GitHubClient instance
        """
        self.client = client

    async def get_repository(self, owner: str, repo: str) -> RepositoryResponse:
        """Get repository details.

        Args:
            owner: Repository owner username
            repo: Repository name

        Returns:
            RepositoryResponse: Repository data
        """
        data = await self.client.get(f"/repos/{owner}/{repo}")
        return RepositoryResponse(**data)


def get_repository_controller(
    token: str = Depends(get_github_token),
) -> RepositoryController:
    """Dependency injection for RepositoryController.

    Args:
        token: GitHub token

    Returns:
        RepositoryController: Instance of controller
    """
    client = GitHubClient(token)
    return RepositoryController(client)

"""Commits controller for GitHub API."""

from typing import List
from fastapi import Depends
from ..utils import GitHubClient
from ..models import CommitResponse, CommitDetailResponse
from .organization import get_github_token


class CommitsController:
    """Controller for commit operations."""

    def __init__(self, client: GitHubClient):
        """Initialize controller with GitHub client.

        Args:
            client: GitHubClient instance
        """
        self.client = client

    async def list_commits(
        self,
        owner: str,
        repo: str,
        per_page: int = 30,
        page: int = 1,
        sha: str = None,
    ) -> List[CommitResponse]:
        """List commits of a repository.

        Args:
            owner: Repository owner username
            repo: Repository name
            per_page: Number of results per page (max 100)
            page: Page number
            sha: Branch or commit SHA (optional)

        Returns:
            List[CommitResponse]: List of commits
        """
        params = {"per_page": min(per_page, 100), "page": page}
        if sha:
            params["sha"] = sha

        data = await self.client.get(
            f"/repos/{owner}/{repo}/commits",
            params=params,
        )
        return [CommitResponse(**commit) for commit in data]

    async def get_commit(
        self,
        owner: str,
        repo: str,
        commit_sha: str,
    ) -> CommitDetailResponse:
        """Get a single commit by SHA.

        Args:
            owner: Repository owner username
            repo: Repository name
            commit_sha: Commit SHA

        Returns:
            CommitDetailResponse: Detailed commit data
        """
        data = await self.client.get(
            f"/repos/{owner}/{repo}/commits/{commit_sha}",
        )
        return CommitDetailResponse(**data)


def get_commits_controller(
    token: str = Depends(get_github_token),
) -> CommitsController:
    """Dependency injection for CommitsController.

    Args:
        token: GitHub token

    Returns:
        CommitsController: Instance of controller
    """
    client = GitHubClient(token)
    return CommitsController(client)

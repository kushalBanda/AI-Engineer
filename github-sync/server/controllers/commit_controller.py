"""Commit controller."""
from core.github_client import GitHubClient


class CommitController:
    """Handle commit operations."""

    def __init__(self):
        self.client = GitHubClient()

    async def list_commits(self, owner: str, repo: str) -> dict:
        """List commits of a repository."""
        return await self.client.get(f"/repos/{owner}/{repo}/commits")

    async def get_commit(self, owner: str, repo: str, sha: str) -> dict:
        """Get a single commit by SHA."""
        return await self.client.get(f"/repos/{owner}/{repo}/commits/{sha}")

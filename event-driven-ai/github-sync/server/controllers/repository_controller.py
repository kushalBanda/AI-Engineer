"""Repository controller."""
from core.github_client import GitHubClient


class RepositoryController:
    """Handle repository operations."""

    def __init__(self):
        self.client = GitHubClient()

    async def get_repository(self, owner: str, repo: str) -> dict:
        """Get repository details."""
        return await self.client.get(f"/repos/{owner}/{repo}")

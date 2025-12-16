"""Pull request controller."""
from core.github_client import GitHubClient


class PullRequestController:
    """Handle pull request operations."""

    def __init__(self):
        self.client = GitHubClient()

    async def list_pull_requests(self, owner: str, repo: str, state: str = "all") -> dict:
        """List all pull requests for a repository."""
        params = {"state": state}
        return await self.client.get(f"/repos/{owner}/{repo}/pulls", params=params)

    async def get_pull_request(self, owner: str, repo: str, pull_number: int) -> dict:
        """Get a single pull request by number."""
        return await self.client.get(f"/repos/{owner}/{repo}/pulls/{pull_number}")

    async def list_pull_request_commits(
        self, owner: str, repo: str, pull_number: int
    ) -> dict:
        """List commits in a pull request."""
        return await self.client.get(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/commits"
        )

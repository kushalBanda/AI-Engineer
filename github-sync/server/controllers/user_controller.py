"""User and organization controller."""
from core.github_client import GitHubClient


class UserController:
    """Handle user and organization operations."""

    def __init__(self):
        self.client = GitHubClient()

    async def get_authenticated_user(self) -> dict:
        """Get authenticated user profile."""
        return await self.client.get("/user")

    async def get_public_user(self, username: str) -> dict:
        """Get public user by username."""
        return await self.client.get(f"/users/{username}")

    async def list_user_organizations(self) -> dict:
        """List organizations for authenticated user."""
        return await self.client.get("/user/orgs")

    async def get_organization(self, org: str) -> dict:
        """Get organization information."""
        return await self.client.get(f"/orgs/{org}")

    async def list_organization_repos(self, org: str) -> dict:
        """List repositories of organization."""
        return await self.client.get(f"/orgs/{org}/repos")

"""Organization and User controller for GitHub API."""

from typing import List
from fastapi import Depends
from ..utils import GitHubClient
from ..models import UserResponse, OrganizationResponse, RepositoryResponse
from ..core.config import get_settings, Settings


def get_github_token(settings: Settings = Depends(get_settings)) -> str:
    """Get GitHub token from settings.

    Args:
        settings: Application settings

    Returns:
        str: GitHub token
    """
    return settings.github_token


class OrganizationController:
    """Controller for organization and user operations."""

    def __init__(self, client: GitHubClient):
        """Initialize controller with GitHub client.

        Args:
            client: GitHubClient instance
        """
        self.client = client

    async def get_authenticated_user(self) -> UserResponse:
        """Get authenticated user profile.

        Returns:
            UserResponse: Authenticated user data
        """
        data = await self.client.get("/user")
        return UserResponse(**data)

    async def list_user_organizations(self) -> List[OrganizationResponse]:
        """List organizations for authenticated user.

        Returns:
            List[OrganizationResponse]: List of organizations
        """
        data = await self.client.get("/user/orgs")
        return [OrganizationResponse(**org) for org in data]

    async def get_organization(self, org: str) -> OrganizationResponse:
        """Get single organization information.

        Args:
            org: Organization name

        Returns:
            OrganizationResponse: Organization data
        """
        data = await self.client.get(f"/orgs/{org}")
        return OrganizationResponse(**data)

    async def list_organization_repos(
        self,
        org: str,
        per_page: int = 30,
        page: int = 1,
    ) -> List[RepositoryResponse]:
        """List repositories of an organization.

        Args:
            org: Organization name
            per_page: Number of results per page (max 100)
            page: Page number

        Returns:
            List[RepositoryResponse]: List of repositories
        """
        params = {"per_page": min(per_page, 100), "page": page}
        data = await self.client.get(f"/orgs/{org}/repos", params=params)
        return [RepositoryResponse(**repo) for repo in data]


def get_organization_controller(
    token: str = Depends(get_github_token),
) -> OrganizationController:
    """Dependency injection for OrganizationController.

    Args:
        token: GitHub token

    Returns:
        OrganizationController: Instance of controller
    """
    client = GitHubClient(token)
    return OrganizationController(client)

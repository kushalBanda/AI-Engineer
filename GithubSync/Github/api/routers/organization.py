"""Organization and User API router."""

from typing import List
from fastapi import APIRouter, Depends
from ..controllers.organization import (
    OrganizationController,
    get_organization_controller,
)
from ..models import UserResponse, OrganizationResponse, RepositoryResponse


router = APIRouter(
    prefix="/org",
    tags=["Organization & Users"],
    responses={
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"},
        404: {"description": "Not Found"},
    },
)


@router.get(
    "/user",
    response_model=UserResponse,
    summary="Get authenticated user profile",
    description="Get the authenticated user's profile information",
)
async def get_authenticated_user(
    controller: OrganizationController = Depends(get_organization_controller),
) -> UserResponse:
    """Get authenticated user profile."""
    return await controller.get_authenticated_user()


@router.get(
    "/user/orgs",
    response_model=List[OrganizationResponse],
    summary="List organizations for authenticated user",
    description="Get list of organizations the authenticated user belongs to",
)
async def list_user_organizations(
    controller: OrganizationController = Depends(get_organization_controller),
) -> List[OrganizationResponse]:
    """List organizations for authenticated user."""
    return await controller.list_user_organizations()


@router.get(
    "/orgs/{org}",
    response_model=OrganizationResponse,
    summary="Get organization information",
    description="Get information about a specific organization",
)
async def get_organization(
    org: str,
    controller: OrganizationController = Depends(get_organization_controller),
) -> OrganizationResponse:
    """Get organization information."""
    return await controller.get_organization(org)


@router.get(
    "/orgs/{org}/repos",
    response_model=List[RepositoryResponse],
    summary="List organization repositories",
    description="Get list of repositories in an organization",
)
async def list_organization_repos(
    org: str,
    per_page: int = 30,
    page: int = 1,
    controller: OrganizationController = Depends(get_organization_controller),
) -> List[RepositoryResponse]:
    """List repositories of an organization."""
    return await controller.list_organization_repos(org, per_page, page)

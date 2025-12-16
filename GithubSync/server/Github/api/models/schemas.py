"""Pydantic schemas for GitHub API responses."""

from typing import Optional, List
from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    """GitHub user response schema."""
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: Optional[str] = None
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool
    name: Optional[str] = None
    company: Optional[str] = None
    blog: Optional[str] = None
    location: Optional[str] = None
    bio: Optional[str] = None
    public_repos: Optional[int] = None
    public_gists: Optional[int] = None
    followers: Optional[int] = None
    following: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class OrganizationResponse(BaseModel):
    """GitHub organization response schema."""
    login: str
    id: int
    node_id: str
    url: str
    repos_url: str
    events_url: str
    hooks_url: str
    issues_url: str
    members_url: str
    public_members_url: str
    avatar_url: str
    description: Optional[str] = None
    name: Optional[str] = None
    company: Optional[str] = None
    blog: Optional[str] = None
    location: Optional[str] = None
    email: Optional[str] = None
    twitter_username: Optional[str] = None
    is_verified: Optional[bool] = None
    has_organization_projects: Optional[bool] = None
    has_repository_projects: Optional[bool] = None
    public_repos: Optional[int] = None
    public_gists: Optional[int] = None
    followers: Optional[int] = None
    following: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class RepositoryResponse(BaseModel):
    """GitHub repository response schema."""
    id: int
    node_id: str
    name: str
    full_name: str
    owner: Optional[UserResponse] = None
    private: bool
    html_url: str
    description: Optional[str] = None
    fork: bool
    url: str
    created_at: str
    updated_at: str
    pushed_at: str
    homepage: Optional[str] = None
    size: int
    stargazers_count: int
    watchers_count: int
    language: Optional[str] = None
    forks_count: int
    open_issues_count: int
    default_branch: str
    topics: List[str] = Field(default_factory=list)
    visibility: str


class CommitResponse(BaseModel):
    """GitHub commit response schema."""
    sha: str
    node_id: str
    url: str
    html_url: str
    comments_url: str
    commit: dict
    author: Optional[UserResponse] = None
    committer: Optional[UserResponse] = None
    parents: List[dict] = Field(default_factory=list)


class CommitDetailResponse(BaseModel):
    """Detailed GitHub commit response schema."""
    sha: str
    node_id: str
    url: str
    html_url: str
    comments_url: str
    commit: dict
    author: Optional[UserResponse] = None
    committer: Optional[UserResponse] = None
    parents: List[dict] = Field(default_factory=list)
    stats: Optional[dict] = None
    files: Optional[List[dict]] = None


class PullRequestResponse(BaseModel):
    """GitHub pull request response schema."""
    id: int
    node_id: str
    number: int
    state: str
    title: str
    user: Optional[UserResponse] = None
    body: Optional[str] = None
    created_at: str
    updated_at: str
    closed_at: Optional[str] = None
    merged_at: Optional[str] = None
    html_url: str
    issue_url: str
    commits_url: str
    review_comments_url: str
    review_comment_url: str
    comments_url: str
    statuses_url: str
    head: Optional[dict] = None
    base: Optional[dict] = None
    locked: bool
    draft: bool
    mergeable: Optional[bool] = None
    merged: bool
    merge_sha: Optional[str] = None
    mergeability_state: Optional[str] = None


class ErrorResponse(BaseModel):
    """Error response schema."""
    message: str
    documentation_url: Optional[str] = None
    status: int = Field(default=400)

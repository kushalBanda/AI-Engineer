import { useState } from 'react'
import { apiService } from '../services/api'
import './OrganizationsList.css'

function OrganizationsList({ organizations, loading, error }) {
  const [selectedOrg, setSelectedOrg] = useState(null)
  const [repos, setRepos] = useState([])
  const [loadingRepos, setLoadingRepos] = useState(false)
  const [repoError, setRepoError] = useState(null)

  const handleOrgClick = async (org) => {
    if (selectedOrg?.login === org.login) {
      setSelectedOrg(null)
      setRepos([])
      return
    }

    setSelectedOrg(org)
    setLoadingRepos(true)
    setRepoError(null)

    try {
      const response = await apiService.getOrgRepos(org.login)
      setRepos(response.data)
    } catch (err) {
      setRepoError(err.response?.data?.detail || 'Failed to fetch repositories')
      console.error('Error fetching repos:', err)
    } finally {
      setLoadingRepos(false)
    }
  }

  if (loading) {
    return (
      <div className="organizations-list">
        <h2 className="section-title">Organizations</h2>
        <div className="loading">Loading organizations...</div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="organizations-list">
        <h2 className="section-title">Organizations</h2>
        <div className="flash-error">
          <svg className="octicon" viewBox="0 0 16 16" fill="currentColor">
            <path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
          </svg>
          {error}
        </div>
      </div>
    )
  }

  return (
    <div className="organizations-list">
      <h2 className="section-title">Organizations</h2>
      
      {organizations.length === 0 ? (
        <div className="empty-state">
          <svg className="octicon-empty" viewBox="0 0 16 16" fill="currentColor">
            <path d="M1.75 16A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0h8.5C11.216 0 12 .784 12 1.75v12.5c0 .085-.006.168-.018.25h2.268a.25.25 0 0 0 .25-.25V8.285a.25.25 0 0 0-.111-.208l-1.055-.703a.749.749 0 1 1 .832-1.248l1.055.703c.487.325.779.871.779 1.456v7.215A1.75 1.75 0 0 1 14.25 16h-3.5a.75.75 0 0 1-.197-.026c-.099.017-.2.026-.303.026h-8.5Zm0-1.5h8.5a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25Zm10.5 0h2.5a.25.25 0 0 0 .25-.25v-7.215a.25.25 0 0 0-.111-.208l-1.055-.703a.749.749 0 1 1 .832-1.248l1.055.703c.487.325.779.871.779 1.456v7.215a.25.25 0 0 1-.25.25h-2.5a.75.75 0 0 1 0-1.5Z"></path>
          </svg>
          <p>You're not a member of any organizations yet.</p>
        </div>
      ) : (
        <div className="orgs-container">
          {organizations.map((org) => (
            <div key={org.id} className="org-item">
              <div 
                className="org-header"
                onClick={() => handleOrgClick(org)}
              >
                <img src={org.avatar_url} alt={org.login} className="org-avatar" />
                <div className="org-info">
                  <h3>{org.name || org.login}</h3>
                  <p className="org-login">{org.login}</p>
                  {org.description && (
                    <p className="org-description">{org.description}</p>
                  )}
                </div>
                <svg 
                  className={`octicon org-toggle ${selectedOrg?.login === org.login ? 'expanded' : ''}`}
                  viewBox="0 0 16 16" 
                  fill="currentColor"
                >
                  <path d="M12.78 6.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 7.28a.749.749 0 1 1 1.06-1.06L8 9.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
                </svg>
              </div>

              {selectedOrg?.login === org.login && (
                <div className="org-repos">
                  {loadingRepos ? (
                    <div className="loading">Loading repositories...</div>
                  ) : repoError ? (
                    <div className="flash-error">
                      <svg className="octicon" viewBox="0 0 16 16" fill="currentColor">
                        <path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
                      </svg>
                      {repoError}
                    </div>
                  ) : repos.length === 0 ? (
                    <div className="empty-state">
                      <p>No repositories found.</p>
                    </div>
                  ) : (
                    <div className="repos-list">
                      {repos.map((repo) => (
                        <a
                          key={repo.id}
                          href={repo.html_url}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="repo-item"
                        >
                          <div className="repo-header">
                            <svg className="octicon repo-icon" viewBox="0 0 16 16" fill="currentColor">
                              <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.757 1.65L2.5 15.5h-1A2.5 2.5 0 0 1 0 13V2.5Z"></path>
                            </svg>
                            <h4>{repo.name}</h4>
                            {repo.private && (
                              <span className="repo-badge">Private</span>
                            )}
                          </div>
                          {repo.description && (
                            <p className="repo-description">{repo.description}</p>
                          )}
                          <div className="repo-meta">
                            {repo.language && (
                              <span className="repo-language">
                                <span className="language-dot"></span>
                                {repo.language}
                              </span>
                            )}
                            <span className="repo-stars">
                              <svg className="octicon" viewBox="0 0 16 16" fill="currentColor">
                                <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z"></path>
                              </svg>
                              {repo.stargazers_count}
                            </span>
                            <span className="repo-forks">
                              <svg className="octicon" viewBox="0 0 16 16" fill="currentColor">
                                <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
                              </svg>
                              {repo.forks_count}
                            </span>
                          </div>
                        </a>
                      ))}
                    </div>
                  )}
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

export default OrganizationsList

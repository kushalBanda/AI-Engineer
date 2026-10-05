import './UserProfile.css'

function UserProfile({ user }) {
  if (!user) {
    return (
      <div className="user-profile">
        <div className="loading">Loading user profile...</div>
      </div>
    )
  }

  return (
    <div className="user-profile">
      <h2 className="section-title">Profile</h2>
      <div className="profile-content">
        <div className="profile-avatar">
          <img src={user.avatar_url} alt={user.login} />
        </div>
        <div className="profile-details">
          <h3 className="profile-name">{user.name || user.login}</h3>
          <p className="profile-username">{user.login}</p>
          {user.bio && <p className="profile-bio">{user.bio}</p>}
          
          {user.location && (
            <p className="profile-meta">
              <svg className="octicon" viewBox="0 0 16 16" fill="currentColor">
                <path d="m12.596 11.596-3.535 3.536a1.5 1.5 0 0 1-2.122 0l-3.535-3.536a6.5 6.5 0 1 1 9.192-9.192 6.5 6.5 0 0 1 0 9.192Zm-1.06-8.132a5 5 0 1 0-7.072 7.072L8 14.07l3.536-3.536a5 5 0 0 0 0-7.072ZM8 9a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 9Z"></path>
              </svg>
              {user.location}
            </p>
          )}

          <div className="profile-stats">
            {user.public_repos !== null && (
              <a href={`https://github.com/${user.login}?tab=repositories`} target="_blank" rel="noopener noreferrer" className="stat-link">
                <span className="stat-value">{user.public_repos}</span>
                <span className="stat-label">repositories</span>
              </a>
            )}
            {user.followers !== null && (
              <a href={`https://github.com/${user.login}?tab=followers`} target="_blank" rel="noopener noreferrer" className="stat-link">
                <span className="stat-value">{user.followers}</span>
                <span className="stat-label">followers</span>
              </a>
            )}
            {user.following !== null && (
              <a href={`https://github.com/${user.login}?tab=following`} target="_blank" rel="noopener noreferrer" className="stat-link">
                <span className="stat-value">{user.following}</span>
                <span className="stat-label">following</span>
              </a>
            )}
          </div>

          <div className="profile-actions">
            <a 
              href={user.html_url} 
              target="_blank" 
              rel="noopener noreferrer"
              className="btn btn-block"
            >
              View on GitHub
            </a>
          </div>
        </div>
      </div>
    </div>
  )
}

export default UserProfile

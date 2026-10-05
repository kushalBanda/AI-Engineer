import { useState, useEffect } from 'react'
import { useNavigate, useSearchParams } from 'react-router-dom'
import { useAuth } from '../contexts/AuthContext'
import { initiateGitHubOAuth, handleOAuthCallback, isOAuthCallback, getOAuthParams, isOAuthConfigured } from '../services/githubOAuth'
import './Login.css'

function Login() {
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const { login, isAuthenticated } = useAuth()
  const navigate = useNavigate()
  const [searchParams] = useSearchParams()

  // Redirect if already authenticated
  useEffect(() => {
    if (isAuthenticated) {
      navigate('/dashboard')
    }
  }, [isAuthenticated, navigate])

  // Handle OAuth callback
  useEffect(() => {
    const handleCallback = async () => {
      if (isOAuthCallback()) {
        setLoading(true)
        setError('')
        
        try {
          const { code, state } = getOAuthParams()
          const token = await handleOAuthCallback(code, state)
          
          const result = await login(token)
          if (result.success) {
            navigate('/dashboard')
          } else {
            setError(result.error || 'Authentication failed')
          }
        } catch (err) {
          setError(err.message || 'Failed to authenticate with GitHub')
          console.error('OAuth error:', err)
        } finally {
          setLoading(false)
        }
      }
    }

    handleCallback()
  }, [login, navigate])

  const handleGitHubSignIn = () => {
    setError('')
    try {
      initiateGitHubOAuth()
    } catch (err) {
      setError(err.message || 'Failed to initiate GitHub sign-in. Please use personal access token instead.')
    }
  }

  // Fallback: Manual token input (if OAuth not configured)
  const [showTokenInput, setShowTokenInput] = useState(false)
  const [token, setToken] = useState('')

  const handleTokenSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setLoading(true)

    if (!token.trim()) {
      setError('Please enter your GitHub token')
      setLoading(false)
      return
    }

    const result = await login(token)
    
    if (result.success) {
      navigate('/dashboard')
    } else {
      setError(result.error || 'Login failed')
    }
    
    setLoading(false)
  }

  if (loading && isOAuthCallback()) {
    return (
      <div className="login-container">
        <div className="login-card">
          <div className="loading-spinner"></div>
          <p>Completing sign in...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="login-container">
      <div className="login-card">
        <div className="login-header">
          <svg height="32" className="github-logo" viewBox="0 0 16 16" fill="currentColor">
            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
          </svg>
          <h1>Sign in to GithubSync</h1>
          <p>Use your GitHub account to continue</p>
        </div>

        {error && (
          <div className="flash-error">
            <svg className="octicon" viewBox="0 0 16 16" fill="currentColor">
              <path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
            </svg>
            {error}
          </div>
        )}

        <div className="login-form">
          {isOAuthConfigured() ? (
            <>
              <button
                onClick={handleGitHubSignIn}
                disabled={loading}
                className="btn btn-primary btn-block"
              >
                <svg className="octicon" viewBox="0 0 16 16" fill="currentColor">
                  <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                </svg>
                Sign in with GitHub
              </button>

              <div className="login-divider">
                <span>or</span>
              </div>
            </>
          ) : null}

          {!showTokenInput ? (
            <button
              onClick={() => setShowTokenInput(true)}
              className={`btn btn-block ${isOAuthConfigured() ? '' : 'btn-primary'}`}
              type="button"
            >
              {isOAuthConfigured() ? 'Use personal access token' : 'Sign in with personal access token'}
            </button>
          ) : (
            <form onSubmit={handleTokenSubmit} className="token-form">
              <div className="form-group">
                <label htmlFor="token">Personal Access Token</label>
                <input
                  type="password"
                  id="token"
                  value={token}
                  onChange={(e) => setToken(e.target.value)}
                  placeholder="ghp_xxxxxxxxxxxxxxxxxxxx"
                  disabled={loading}
                  className="form-control"
                />
                <p className="form-note">
                  <a 
                    href="https://github.com/settings/tokens" 
                    target="_blank" 
                    rel="noopener noreferrer"
                  >
                    Generate a token
                  </a>
                </p>
              </div>
              <button 
                type="submit" 
                disabled={loading}
                className="btn btn-primary btn-block"
              >
                {loading ? 'Signing in...' : 'Sign in'}
              </button>
            </form>
          )}
        </div>

        <div className="login-footer">
          <p className="text-muted">
            By signing in, you agree to our terms of service and privacy policy.
          </p>
        </div>
      </div>
    </div>
  )
}

export default Login

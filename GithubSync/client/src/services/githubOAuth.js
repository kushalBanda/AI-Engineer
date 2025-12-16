/**
 * GitHub OAuth Service
 * Handles GitHub OAuth authentication flow
 * 
 * SECURITY NOTE: In production, the token exchange should be done server-side
 * to protect the client secret. This client-side implementation is for development/learning.
 */

// GitHub OAuth Configuration
// You'll need to create a GitHub OAuth App at: https://github.com/settings/developers
const GITHUB_CLIENT_ID = import.meta.env.VITE_GITHUB_CLIENT_ID || ''
const GITHUB_REDIRECT_URI = import.meta.env.VITE_GITHUB_REDIRECT_URI || 
  `${window.location.origin}/auth/callback`

// Check if OAuth is configured
export const isOAuthConfigured = () => {
  return !!GITHUB_CLIENT_ID
}

// Scopes required for the app
const GITHUB_SCOPES = ['read:user', 'read:org', 'repo']

/**
 * Initiate GitHub OAuth flow
 */
export function initiateGitHubOAuth() {
  if (!GITHUB_CLIENT_ID) {
    throw new Error('GitHub OAuth is not configured. Please set VITE_GITHUB_CLIENT_ID in your .env file.')
  }

  const params = new URLSearchParams({
    client_id: GITHUB_CLIENT_ID,
    redirect_uri: GITHUB_REDIRECT_URI,
    scope: GITHUB_SCOPES.join(' '),
    state: generateState(),
  })

  // Store state for verification
  sessionStorage.setItem('github_oauth_state', params.get('state'))

  // Redirect to GitHub
  window.location.href = `https://github.com/login/oauth/authorize?${params.toString()}`
}

/**
 * Handle OAuth callback
 * Exchange authorization code for access token
 */
export async function handleOAuthCallback(code, state) {
  // Verify state
  const storedState = sessionStorage.getItem('github_oauth_state')
  if (!storedState || storedState !== state) {
    throw new Error('Invalid state parameter')
  }

  sessionStorage.removeItem('github_oauth_state')

  try {
    // Exchange code for token
    // Note: In production, this should be done server-side for security
    // For now, we'll use a proxy endpoint or handle it client-side
    const response = await fetch('https://github.com/login/oauth/access_token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify({
        client_id: GITHUB_CLIENT_ID,
        client_secret: import.meta.env.VITE_GITHUB_CLIENT_SECRET || '',
        code,
        redirect_uri: GITHUB_REDIRECT_URI,
        state,
      }),
    })

    if (!response.ok) {
      throw new Error('Failed to exchange code for token')
    }

    const data = await response.json()
    
    if (data.error) {
      throw new Error(data.error_description || data.error)
    }

    return data.access_token
  } catch (error) {
    console.error('OAuth callback error:', error)
    throw error
  }
}

/**
 * Generate random state for OAuth security
 */
function generateState() {
  return Math.random().toString(36).substring(2, 15) + 
         Math.random().toString(36).substring(2, 15)
}

/**
 * Check if we're in OAuth callback
 */
export function isOAuthCallback() {
  const urlParams = new URLSearchParams(window.location.search)
  return urlParams.has('code') && urlParams.has('state')
}

/**
 * Get OAuth callback parameters
 */
export function getOAuthParams() {
  const urlParams = new URLSearchParams(window.location.search)
  return {
    code: urlParams.get('code'),
    state: urlParams.get('state'),
  }
}


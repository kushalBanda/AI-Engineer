import axios from 'axios'

// Base URL for your Python API
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

// Create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Add token to requests if available
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('github_token')
    if (token) {
      // Your backend expects: Authorization: token {token}
      config.headers.Authorization = `token ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Handle response errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Unauthorized - clear token and redirect to login
      localStorage.removeItem('github_token')
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

// API methods
export const apiService = {
  // User endpoints
  getUser: () => api.get('/org/user'),
  
  // Organization endpoints
  getUserOrgs: () => api.get('/org/user/orgs'),
  getOrg: (orgName) => api.get(`/org/orgs/${orgName}`),
  getOrgRepos: (orgName, page = 1, perPage = 30) => 
    api.get(`/org/orgs/${orgName}/repos`, { params: { page, per_page: perPage } }),
  
  // Repository endpoints
  getRepository: (owner, repo) => api.get(`/repos/${owner}/${repo}`),
  getCommits: (owner, repo, page = 1, perPage = 30) => 
    api.get(`/repos/${owner}/${repo}/commits`, { params: { page, per_page: perPage } }),
  
  // Pull Request endpoints
  getPullRequests: (owner, repo, state = 'all', page = 1, perPage = 30) => 
    api.get(`/repos/${owner}/${repo}/pulls`, { params: { state, page, per_page: perPage } }),
}

export default api


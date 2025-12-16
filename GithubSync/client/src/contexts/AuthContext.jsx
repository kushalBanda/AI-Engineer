import { createContext, useContext, useState, useEffect } from 'react'
import { apiService } from '../services/api'

// Create Auth Context
const AuthContext = createContext(null)

// Custom hook to use auth context
export function useAuth() {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider')
  }
  return context
}

// Auth Provider Component
export function AuthProvider({ children }) {
  const [isAuthenticated, setIsAuthenticated] = useState(false)
  const [loading, setLoading] = useState(true)
  const [user, setUser] = useState(null)
  const [error, setError] = useState(null)

  // Check if user is authenticated on mount
  useEffect(() => {
    checkAuth()
  }, [])

  // Check authentication status
  const checkAuth = async () => {
    const token = localStorage.getItem('github_token')
    
    if (!token) {
      setLoading(false)
      setIsAuthenticated(false)
      return
    }

    try {
      // Verify token by fetching user profile
      const response = await apiService.getUser()
      setUser(response.data)
      setIsAuthenticated(true)
      setError(null)
    } catch (err) {
      // Token is invalid
      localStorage.removeItem('github_token')
      setIsAuthenticated(false)
      setUser(null)
      setError(err.response?.data?.detail || 'Authentication failed')
    } finally {
      setLoading(false)
    }
  }

  // Login function
  const login = async (token) => {
    try {
      setLoading(true)
      setError(null)
      
      // Store token temporarily to test it
      localStorage.setItem('github_token', token)
      
      // Verify token by fetching user profile
      const response = await apiService.getUser()
      setUser(response.data)
      setIsAuthenticated(true)
      
      return { success: true }
    } catch (err) {
      localStorage.removeItem('github_token')
      const errorMessage = err.response?.data?.detail || 'Invalid GitHub token'
      setError(errorMessage)
      setIsAuthenticated(false)
      setUser(null)
      return { success: false, error: errorMessage }
    } finally {
      setLoading(false)
    }
  }

  // Logout function
  const logout = () => {
    localStorage.removeItem('github_token')
    setIsAuthenticated(false)
    setUser(null)
    setError(null)
  }

  const value = {
    isAuthenticated,
    loading,
    user,
    error,
    login,
    logout,
    checkAuth,
  }

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}


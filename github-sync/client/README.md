# GithubSync React Client

A modern React application for syncing and viewing GitHub data, styled to match GitHub's clean design.

## 🚀 Getting Started

### Prerequisites
- **Bun** (recommended) or Node.js 16+ with npm
- Your Python API server running on `http://localhost:8000`

### Installing Bun

If you don't have Bun installed:
```bash
curl -fsSL https://bun.sh/install | bash
```

Then restart your terminal or run:
```bash
exec /bin/zsh  # or exec /bin/bash
```

### Installation

1. Install dependencies:
```bash
bun install
```

**Note**: You can also use `npm install` if you prefer npm, but Bun is faster! 🚀

2. (Optional) Set up GitHub OAuth:
   - Create a GitHub OAuth App at [https://github.com/settings/developers](https://github.com/settings/developers)
   - Copy `.env.example` to `.env` and add your OAuth credentials
   - **Note**: For production, OAuth token exchange should be done server-side for security

3. Start the development server:
```bash
bun run dev
```

The app will be available at `http://localhost:3000`

## 🔐 Authentication

The app supports two authentication methods:

### 1. GitHub OAuth (Recommended)
Click "Sign in with GitHub" to use OAuth flow. You'll need to set up a GitHub OAuth App first.

### 2. Personal Access Token (Fallback)
If OAuth isn't configured, you can use a personal access token:
- Go to [GitHub Settings → Developer settings → Personal access tokens](https://github.com/settings/tokens)
- Generate a new token with `repo` and `read:org` scopes
- Click "Use personal access token" on the login page

## 📚 Learning React - Key Concepts Used

### 1. **Components**
React apps are built with components - reusable pieces of UI. Each component is a JavaScript function that returns JSX (HTML-like syntax).

Example: `Login.jsx` is a component that renders a login form.

### 2. **State Management**
We use `useState` hook to manage component state (like form inputs, loading states).

```jsx
const [token, setToken] = useState('')
```

### 3. **Context API**
`AuthContext` provides authentication state to all components without prop drilling. This is React's built-in state management solution.

### 4. **React Router**
Handles navigation between pages (Login → Dashboard).

### 5. **useEffect Hook**
Runs side effects (like API calls) when components mount or when dependencies change.

### 6. **Props**
Components receive data through props (like `user={user}`).

## 🏗️ Project Structure

```
src/
├── components/          # UI components
│   ├── Login.jsx       # Login page
│   ├── Dashboard.jsx   # Main dashboard
│   ├── UserProfile.jsx # User profile display
│   └── OrganizationsList.jsx # Organizations display
├── contexts/           # React Context providers
│   └── AuthContext.jsx # Authentication state
├── services/           # API service layer
│   └── api.js          # API client
├── App.jsx             # Main app component with routes
└── main.jsx            # Entry point
```

## 🔐 Authentication Flow

1. User signs in via GitHub OAuth or enters personal access token
2. Token is validated by calling `/org/user` endpoint
3. If valid, token is stored in localStorage
4. Token is automatically added to all API requests
5. Protected routes check authentication status

## 📡 API Integration

The `api.js` service uses axios to make HTTP requests to your Python backend. All requests automatically include the GitHub token in the Authorization header.

## 🎨 Design

- **GitHub-inspired theme**: Matches GitHub's design system and color scheme
- Clean, minimal interface
- Responsive layout
- CSS custom properties for consistent theming

## 🛠️ Available Scripts

Using Bun (recommended):
- `bun run dev` - Start development server
- `bun run build` - Build for production
- `bun run preview` - Preview production build

Using npm (alternative):
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build

### Why Bun?
- ⚡ **Faster**: Bun installs packages 2-3x faster than npm
- 🚀 **Built-in**: No need for separate Node.js installation
- 📦 **Compatible**: Works with all npm packages
- 🔧 **Simple**: Same commands, better performance

## 🔍 Key React Concepts Explained

### JSX
JSX lets you write HTML-like syntax in JavaScript:
```jsx
return <div>Hello {user.name}</div>
```

### Hooks
Hooks let you use state and other React features in functional components:
- `useState` - manage state
- `useEffect` - side effects
- `useContext` - access context

### Conditional Rendering
```jsx
{isAuthenticated ? <Dashboard /> : <Login />}
```

### Event Handlers
```jsx
<button onClick={handleClick}>Click me</button>
```

## 🚦 Next Steps

Try modifying:
1. Add more GitHub data (commits, pull requests)
2. Add error boundaries for better error handling
3. Add loading skeletons
4. Implement pagination for repositories
5. Add search functionality


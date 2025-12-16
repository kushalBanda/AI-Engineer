# Bun Quick Reference Guide

## What is Bun?

**Bun** is a fast JavaScript runtime, bundler, test runner, and package manager - all in one! It's designed to be a drop-in replacement for Node.js and npm.

## 🎯 Why Use Bun?

1. **Speed**: Installs packages 2-3x faster than npm
2. **Simplicity**: One tool instead of multiple (Node.js + npm + others)
3. **Compatibility**: Works with all npm packages
4. **Built-in**: Includes bundler, test runner, and more

## 📦 Bun Commands vs npm

| Task | npm | Bun |
|------|-----|-----|
| Install dependencies | `npm install` | `bun install` |
| Add a package | `npm install <package>` | `bun add <package>` |
| Add dev dependency | `npm install -D <package>` | `bun add -d <package>` |
| Remove package | `npm uninstall <package>` | `bun remove <package>` |
| Run script | `npm run dev` | `bun run dev` |
| Run directly | `npx <command>` | `bunx <command>` |

## 🚀 Common Commands for This Project

### Development
```bash
# Start dev server
bun run dev

# Build for production
bun run build

# Preview production build
bun run preview
```

### Package Management
```bash
# Install all dependencies
bun install

# Add a new package
bun add axios

# Add a dev dependency
bun add -d @types/react

# Remove a package
bun remove axios
```

## 🔄 Migrating from npm

If you already have `node_modules` installed with npm:
1. Just run `bun install` - Bun will use the existing `package.json`
2. Bun creates `bun.lockb` (binary lockfile) instead of `package-lock.json`
3. Everything else works the same!

## 💡 Tips

- **Faster installs**: Bun uses a binary lockfile format, making installs faster
- **Same package.json**: Your existing `package.json` works perfectly with Bun
- **No changes needed**: All your scripts and dependencies work as-is
- **Drop-in replacement**: You can switch between npm and Bun anytime

## 🎓 Learning React with Bun

When learning React, Bun makes things faster:
- Faster installs = less waiting
- Same commands = easy to learn
- Better performance = smoother development

## ❓ FAQ

**Q: Do I need Node.js if I use Bun?**  
A: No! Bun includes its own JavaScript runtime.

**Q: Can I use npm packages with Bun?**  
A: Yes! Bun is 100% compatible with npm packages.

**Q: Can I switch back to npm?**  
A: Yes! Just use `npm install` instead. Both work with the same `package.json`.

**Q: Is Bun production-ready?**  
A: Yes! Bun is stable and used in production by many companies.

## 🎉 That's it!

You're now using Bun! Everything works the same, just faster. Happy coding! 🚀


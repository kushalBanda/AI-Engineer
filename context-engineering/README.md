# Context engineering

[← AI Engineer](../README.md)

**Level:** 🟡 Intermediate · **Type:** `Reference` · Commands run from the repo root.

A template for context engineering: giving AI coding assistants all the information they need to finish a job end to end. Prompt engineering is about wording a task, like handing someone a sticky note. Context engineering is a full system of documentation, examples, rules, patterns, and validation, like handing them a screenplay.

Why it matters:

1. **Fewer failures.** Most agent failures are context failures, not model failures.
2. **Consistency.** The AI follows your project's patterns and conventions.
3. **Complex features.** Multi-step work becomes possible with the right context.
4. **Self-correction.** Validation loops let the AI fix its own mistakes.

## What's in the folder

```
context-engineering/
├── .claude/commands/
│   ├── generate-prp.md        # Generates comprehensive PRPs
│   └── execute-prp.md         # Executes PRPs to implement features
├── PRPs/
│   ├── templates/prp_base.md  # Base template for PRPs
│   └── EXAMPLE_multi_agent_prp.md
├── examples/                  # Your code examples (critical!)
├── CLAUDE.md                  # Global rules for the AI assistant
├── INITIAL.md                 # Template for feature requests
└── INITIAL_EXAMPLE.md         # Example feature request
```

## Quick start (in Claude Code)

1. Edit `CLAUDE.md` with your project rules: project awareness, code structure, testing, style, and documentation standards.
2. Put relevant code examples in `examples/`.
3. Describe the feature in `INITIAL.md`. See `INITIAL_EXAMPLE.md`.
4. Generate a PRP (Product Requirements Prompt): `/generate-prp INITIAL.md`
5. Run it: `/execute-prp PRPs/your-feature-name.md`

The slash commands live in `.claude/commands/`. `$ARGUMENTS` receives whatever you pass after the command name.

## Writing `INITIAL.md`

```markdown
## FEATURE:
[What you want to build. Be specific about functionality and requirements]

## EXAMPLES:
[Example files in examples/ and how to use them]

## DOCUMENTATION:
[Links to relevant docs, APIs, or MCP server resources]

## OTHER CONSIDERATIONS:
[Gotchas, specific requirements, things AI assistants often miss]
```

- **Feature:** be specific. Not "Build a web scraper" but "Build an async web scraper using BeautifulSoup that extracts product data from e-commerce sites, handles rate limiting, and stores results in PostgreSQL."
- **Examples:** point to files in `examples/` and say what to copy.
- **Documentation:** API docs, library guides, MCP server docs, database schemas.
- **Other considerations:** auth, rate limits, common pitfalls, performance needs.

## The PRP workflow

A PRP is like a PRD, but written to instruct an AI coding assistant: full context, implementation steps with validation gates, error handling patterns, and test requirements.

- `/generate-prp` reads the feature request, researches the codebase for patterns, gathers docs and gotchas, writes a step-by-step plan with validation gates, and scores its confidence from 1 to 10.
- `/execute-prp` loads the PRP, plans with a task list, implements each part, runs tests and linting, fixes issues, and checks every success criterion.

See `PRPs/EXAMPLE_multi_agent_prp.md` for a full example.

## Using examples well

AI assistants do much better when they can see patterns. Include code structure (modules, imports, class and function patterns), testing (file layout, mocking, assertions), integrations (API clients, database connections, auth), and CLI patterns (argument parsing, output, error handling).

## Best practices

1. Be explicit in `INITIAL.md`. Don't assume the AI knows your preferences.
2. Provide plenty of examples, including what not to do.
3. Use validation gates. PRPs include test commands that must pass.
4. Include official docs and specific sections.
5. Customize `CLAUDE.md` with your conventions.

Resources: [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code) · [Context engineering best practices](https://www.philschmid.de/context-engineering)

# Contributing

Thanks for helping. This repo is a set of runnable AI engineering modules. Each top-level folder is one module. The root `README.md` is the map of all modules. A module with run steps or code also has its own `README.md` with the full guide (see below).

## Ways to help

- Fix a bug or a broken run step in a module.
- Improve a module's README, or its section in the root `README.md`.
- Add a new module.
- Report a problem with an [issue](../../issues/new/choose).

For a new module, open a **Module proposal** issue first. This avoids work on a topic that is already covered.

## Set up

1. Fork the repo and clone your fork.
2. Create a branch: `git checkout -b feat/<short-name>`.
3. Python modules use [uv](https://docs.astral.sh/uv/) and Python 3.13 or newer.
4. TypeScript modules use a current Node.js LTS.

## Add a module

1. Create one new top-level folder. Use lowercase words with hyphens, for example `vector-search-basics`.
2. Make the run steps work from a clean clone. Test them before you open the PR.
3. Add a `.env.example` if the module reads a `.env`. List variable names only.
4. If the module has run steps or code, add a `README.md` to its folder from [`.github/MODULE_README_TEMPLATE.md`](.github/MODULE_README_TEMPLATE.md) (see [Module READMEs](#module-readmes)).
5. Add the module to the root `README.md`:
   - Copy [`.github/MODULE_SECTION_TEMPLATE.md`](.github/MODULE_SECTION_TEMPLATE.md) into the area it belongs to: Agents, Model Context Protocol (MCP), Memory, retrieval, and RAG, Prompting and context engineering, AI applications, APIs and integrations, Deployment and MLOps, or Model training. If none fits, propose a new area in your PR.
   - Add it to the area's module table, the **Module map**, and **Prerequisites at a glance**.
   - Add the section to the **Contents** list.
   - Areas are grouped by topic, not by level or folder order. Give each module a level label instead.

### Module READMEs

The root `README.md` stays free of code. It says what each module builds, what it needs, and where to start.

- **A module with run steps or code** gets its own `README.md` with the full guide: files, run commands, examples, and dependencies. Its root section is a short summary and a 📘 link to that guide.
- **A module with nothing to run**, such as a reading list or a notebook you open and run top to bottom, can live entirely in its root section. `ai-dev-prompts/` and `huggingface-finetuning/` work this way.

Keep every module's rows in the Module map and Prerequisites tables either way.

### Type tags

| Tag | Use it for |
| :--- | :--- |
| `Project` | A runnable app |
| `Tutorial` | A set of small scripts |
| `Course` | An ordered series of lessons |
| `Reference` | Material to read |

### Levels

| Level | Use it for |
| :--- | :--- |
| Beginner | One idea, or a small deploy |
| Intermediate | Agents, memory, voice, and pipelines |
| Advanced | Full services and production patterns |

## Secrets

Never commit a secret. This includes API keys, tokens, passwords, and service account files.

- Commit `.env.example` with names only. Never commit `.env`.
- Read keys from the environment, for example `os.getenv("OPENAI_API_KEY")`.
- A CI check scans every pull request with [gitleaks](https://github.com/gitleaks/gitleaks). A leaked key fails the check.
- If you commit a key by mistake, revoke the key first. Then remove it from the branch.

## Pull requests

1. Keep each PR to one change.
2. Use a clear title, for example `fix: correct the Redis port in redis-basics`.
3. Fill in the PR template.
4. Confirm that the checks pass.

A maintainer reviews each PR. You may get change requests. This is normal.

## Conduct

All contributors must follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

When you contribute, you agree that your work uses the [MIT License](LICENSE).

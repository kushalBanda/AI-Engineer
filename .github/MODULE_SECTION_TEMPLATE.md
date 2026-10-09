<!--
Copy this into the root README.md, under the right tier
(Beginner, Intermediate, or Advanced modules). Also add a row
for the module to the "Projects by difficulty" table and a
link in the table of contents. Modules don't have their own README.
-->

### Module name

🟢 Beginner · `Tutorial` · [`module-name/`](./module-name)

One or two sentences. Say what the module builds and why it is useful.

| Path | What it shows |
| :--- | :--- |
| `path/to/file.py` | What this file does |

**Run**

```bash
cd module-name
cp .env.example .env   # only if the module reads a .env
uv run python path/to/file.py
```

State the exact commands. A reader must run them from a clean clone.

**Depends on**

- Services the module needs, for example Redis on `localhost:6379`.
- API keys the module reads, by name only.
- Language and tool versions.

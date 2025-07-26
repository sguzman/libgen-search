# 🤖 AGENT.md — Contribution Guidelines for AI Agents

This document defines how AI agents should assist in the development of **LibGen CLI**, a command-line Python tool for searching and downloading books from Library Genesis.

It ensures that agent-generated code aligns with project goals, design principles, and technical standards.

---

## 🧠 Project Intent (from `README.md`)

LibGen CLI is a terminal-based utility that:
- Searches across LibGen mirrors
- Filters out low-quality, duplicate, and non-book entries
- Prompts user to select books and preferred formats
- Outputs `aria2c`-compatible `urls.txt` with sanitized filenames

The project emphasizes:
- ✨ Clean and maintainable UX
- ⚙️ Reliable download workflows
- 🧹 Output hygiene (no broken links or messy filenames)

---

## 📦 Runtime & Dev Stack

> **Dependency and environment management is handled exclusively with [`rye`](https://rye-up.com)**

Agents should **not** write instructions involving `pip`, `venv`, or `poetry`.

### ✅ Python Environment
- Python version: pinned via `.python-version` or `pyproject.toml` (assumed Python 3.11+)
- Dependency manager: [`rye`](https://rye-up.com)

### ✅ Formatting & Linting
- Auto-formatting: [`ruff format`](https://docs.astral.sh/ruff/formatter/)
- Linting: [`ruff check`](https://docs.astral.sh/ruff/)
- Agents must only emit code that conforms to `ruff` style rules.
  - Avoid unused imports, overly long lines, and unnecessary comments.
  - Reuse imports, avoid repetition, follow standard idioms.

---

## 🔨 Code Architecture (inspired by `ROADMAP.md`)

All logic must be modular and split by purpose. Use the following structure unless otherwise updated:

```

libgen\_cli/
├── libgen\_cli.py         # CLI entrypoint
├── search.py             # Mirror querying and HTML parsing
├── filter.py             # Duplicate and non-book filtering
├── format.py             # Filename cleaning and format selection
├── urls.py               # URL builder and urls.txt writer
├── utils.py              # Misc helpers (slugify, size parsing, etc.)
├── requirements.lock     # Auto-managed by Rye
├── README.md
├── ROADMAP.md
├── AGENT.md
└── LICENSE

````

> ✅ Agents should update `ROADMAP.md` progress by checking off relevant subgoals when a change is committed or submitted.

---

## 📋 CLI Principles

Use [Typer](https://typer.tiangolo.com/) or [argparse] initially, and follow these guidelines:

- Prefer **declarative flags** over positional args when possible
- Maintain **scriptability** and **non-interactive mode** fallback
- Output to `stdout` or `.txt` in project root only (no stray files)

---

## 🧪 Testing Best Practices

If testing is added (Phase 6), AI-generated tests should:
- Use `pytest`
- Avoid large fixtures; use small representative examples
- Test modules individually (unit tests) before integrating

---

## 📄 When Writing Code...

- ✅ Always include `ruff`-clean code with no warnings
- ✅ Include descriptive inline comments when logic is non-trivial
- ✅ Include docstrings in all functions and modules
- ✅ Provide readable logging or CLI print feedback (e.g., progress, filtered count)

```python
# Good example
def filter_duplicates(entries: list[BookEntry]) -> list[BookEntry]:
    """
    Remove duplicates by comparing title, author, and year (case-insensitive).
    """
    seen = set()
    filtered = []
    for entry in entries:
        key = (entry.title.lower(), entry.author.lower(), entry.year)
        if key not in seen:
            seen.add(key)
            filtered.append(entry)
    return filtered
````

---

## 🧼 When Writing Output

* Filenames should be:

  * Slugified
  * Short enough for Windows paths
  * Free of weird Unicode or unsafe characters

```bash
out="Modern_Physics_-_K_Taylor.pdf"
```

---

## 🤝 Commit Guidance (for Git-integrated agents)

* ✅ Use conventional commits:

  * `feat: add search logic for first mirror`
  * `fix: sanitize filenames to avoid quotes`
  * `refactor: split filter logic into filter.py`
* ✅ Group related changes logically (1 module per commit ideally)
* ✅ Update ROADMAP.md checkboxes if completing a subgoal

---

## 📬 AI Contribution Workflow

1. Follow `README.md` for project scope
2. Reference `ROADMAP.md` for current phase goals
3. Generate modules incrementally, not monolithically
4. Write clean, `ruff`-formatted code
5. Update AGENT.md or ROADMAP.md if changing functionality or structure

---

## 🧠 Final Notes

This is a **user-facing CLI tool** for a technically proficient audience. Prioritize:

* UX clarity
* High reliability
* Output precision
* Code maintainability

Agents should ask before adding advanced features not yet scheduled in the roadmap.

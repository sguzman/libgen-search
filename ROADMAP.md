## ✅ Phase 1 — Minimal MVP

> Goal: Search LibGen from the CLI, clean up results, and output a functional `urls.txt`.

- [x] CLI boilerplate with Rye (`libgen_cli.py`)
- [x] Implement basic search against one LibGen mirror (HTML scraping)
- [x] Parse results into structured Python objects
- [x] Filter out non-book/journal entries
- [x] Remove obvious duplicates (same title + author + year)
- [x] Let user interactively select desired entries via CLI
- [x] Output `urls.txt` with proper `out="..."` syntax
- [x] Confirm it works with `aria2c -i urls.txt`

---

## 🚧 Phase 2 — Mirror Robustness & Format Choice

> Goal: Make search more reliable and let users pick formats (PDF, EPUB, etc.)

- [ ] Add fallback logic for multiple LibGen mirrors
- [ ] Group results by title; let user pick preferred format(s)
- [ ] Auto-skip broken/inaccessible mirror links
- [ ] Sort by size or quality heuristics (optional)
- [ ] Improve filename sanitation for `out=...`
- [ ] Add flag to auto-select best format (non-interactive mode)

---

## 🧠 Phase 3 — Usability & CLI Options

> Goal: Improve user experience and make the CLI scriptable.

- [ ] `--format` flag to pre-select format
- [ ] `--max-results` and `--min-size` filters
- [ ] `--non-interactive` mode (auto-pick best version of each book)
- [ ] Pretty table/box output with `rich`
- [ ] Save query results to JSON for offline inspection

---

## 🔄 Phase 4 — Parallelism, Caching, and Retry Logic

> Goal: Handle flaky mirrors and allow repeat queries without re-downloading metadata.

- [ ] Retry on failed mirror fetches
- [ ] Use local cache for previously fetched books (by md5 or title)
- [ ] Option to re-use `urls.txt` without prompting again
- [ ] Parallel mirror polling to speed up lookups

---

## 🧩 Phase 5 — Metadata Enrichment & Integration

> Goal: Enhance results with better metadata and support library tools.

- [ ] Fetch additional metadata (ISBN, cover image, description) via Open Library or other APIs
- [ ] Add `--json` output format with full book metadata
- [ ] Calibre-compatible metadata export (`.opf`)
- [ ] Optional metadata tagging in filenames

---

## 🧪 Phase 6 — Testing, Packaging & Release

> Goal: Make the project easy to install, test, and share.

- [ ] Add unit tests for each module (`pytest`)
- [ ] Auto-format and lint (`black`, `ruff`)
- [ ] CLI autocompletion with `typer`
- [ ] Publish to PyPI
- [ ] Precompiled Windows/Linux binaries with `shiv` or `pynsist`

---

## ✨ Stretch Goals

> Cool ideas that may be implemented after core goals are complete.

- [ ] TUI app using `textual` or `urwid`
- [ ] Web front-end for query + download
- [ ] GUI wrapper using `PyQt` or `tkinter`
- [ ] Search LibGen fiction, comics, and scientific articles separately
- [ ] RAG integration (ask LLMs to recommend LibGen books)

---

## 📌 Notes

- File naming will follow slugified format: `Title_-_Author.pdf`
- Results will be deduplicated using normalized (lowercase, no punctuation) keys

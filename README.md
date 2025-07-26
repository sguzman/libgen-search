# 📚 LibGen CLI — Search and Download Tool for Library Genesis

**LibGen CLI** is a Python command-line tool designed to search for books on [Library Genesis](http://libgen.rs) across multiple mirrors, clean up and deduplicate the results, and let users select which books to download. It outputs a clean, `aria2c`-compatible `urls.txt` file with user-friendly filenames, allowing high-performance batch downloads.

---

## 🔥 Goals

- ✅ **Mirror-Agnostic Search** — Automatically query multiple LibGen mirrors for reliability
- ✅ **Clean, Usable Results** — Filter out:
  - Journal articles
  - Broken entries or "duds"
  - Duplicates across formats
- ✅ **Interactive Format/Book Selection**
- ✅ **Output for High-Speed Downloaders** — Generate a `urls.txt` for use with [`aria2c`](https://aria2.github.io/)
- ✅ **Readable Filenames** — Automatically set proper `out=` values for clean, human-friendly filenames

---

## 🧰 Features

- 🔍 Search across multiple LibGen mirrors
- 🧼 Smart filtering of non-books, bad entries, and duplicates
- 🗂 Choose specific formats (PDF, EPUB, MOBI, DJVU, etc.)
- 🧾 Outputs a ready-to-use `urls.txt` with:
  ```bash
  http://libgen.rs/...&md5=abcdef123...  out="Book_Title_-_Author_Name.pdf"


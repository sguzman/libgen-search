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
````

* ⚙️ Built-in support for [`aria2c -i urls.txt`](https://aria2.github.io/manual/en/html/aria2c.html#cmdoption-i)

---

## 📦 Installation (with [Rye](https://rye-up.com/))

> Rye is the default and recommended Python environment manager for this project.

1. **Install Rye (if not already):**

```bash
   curl -sSf https://rye-up.com/get | bash
```

2. **Clone the repository:**

```bash
   git clone https://github.com/YOUR_USERNAME/libgen-cli
   cd libgen-cli
```

3. **Install dependencies via Rye:**

```bash
   rye sync
```

4. **Run the CLI:**

```bash
   rye run python libgen_cli.py search "theory of computation"
```

---

## 🚀 Usage

### 📖 Basic Search

```bash
rye run python libgen_cli.py search "calculus made easy"
```

### 🧠 Interactive Selection

You will be prompted to choose:

* Desired books from cleaned results
* Preferred formats (PDF, EPUB, etc.)

### 📝 Output

At the end, you'll get a `urls.txt` like this:

```
http://libgen.rs/get.php?md5=a1b2c3d4e5f6...  out="Calculus_Made_Easy_-_Silvanus_Thompson.pdf"
http://libgen.rs/get.php?md5=f6e5d4c3b2a1...  out="Another_Great_Calculus_Book.epub"
```

You can download everything at once using:

```bash
aria2c -i urls.txt
```

---

## ⚠️ Disclaimer

This tool is intended strictly for **educational**, **personal use**, or retrieving **public domain works**. Users are responsible for complying with local copyright laws and the ethical use of online resources.

---

## 🛠 Planned Features

* [ ] Parallel mirror failover
* [ ] Search by author / year / ISBN
* [ ] Hash-based caching
* [ ] JSON output mode
* [ ] Integration with Calibre

---

## 🤝 Contributing

Pull requests are welcome! Please:

* Use `rye` for dependency and virtual environment management
* Format with `black` and `ruff`
* Test before submitting

---

## 📄 License

CC0-1.0 License. See [LICENSE](LICENSE) for full terms.


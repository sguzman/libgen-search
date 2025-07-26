"""Filtering utilities for LibGen search results."""

from __future__ import annotations

from typing import Iterable, List

from search import BookEntry

ALLOWED_EXTENSIONS = {"pdf", "epub", "mobi", "djvu"}


def is_book(entry: BookEntry) -> bool:
    """Return True if the entry looks like a book."""
    title_lower = entry.title.lower()
    if any(word in title_lower for word in ["journal", "issue", "volume", "vol."]):
        return False
    return entry.extension.lower() in ALLOWED_EXTENSIONS


def filter_non_books(entries: Iterable[BookEntry]) -> List[BookEntry]:
    """Filter out entries that are likely not books."""
    return [e for e in entries if is_book(e)]


def deduplicate(entries: Iterable[BookEntry]) -> List[BookEntry]:
    """Remove duplicates based on title, author, and year."""
    seen: set[tuple[str, str, str]] = set()
    unique: list[BookEntry] = []
    for entry in entries:
        key = (entry.title.lower(), entry.author.lower(), entry.year)
        if key not in seen:
            seen.add(key)
            unique.append(entry)
    return unique

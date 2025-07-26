"""Filename formatting utilities."""

from __future__ import annotations

from search import BookEntry
from utils import slugify


def build_filename(entry: BookEntry) -> str:
    """Return a sanitized filename for the given entry."""
    title = slugify(entry.title)
    author = slugify(entry.author)
    return f"{title}_-_{author}.{entry.extension}"

"""Utility helpers for LibGen CLI."""

from __future__ import annotations

import re
import unicodedata


def slugify(value: str) -> str:
    """Return an ASCII-only slug suitable for filenames."""
    normalized = unicodedata.normalize("NFKD", value)
    encoded = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^A-Za-z0-9]+", "_", encoded)
    return slug.strip("_")

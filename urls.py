"""Utilities for writing urls.txt."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from format import build_filename
from search import BookEntry


def write_urls(entries: Iterable[BookEntry], path: str = "urls.txt") -> Path:
    """Write download URLs with ``out=`` filenames to ``urls.txt``."""
    lines = [f'{e.download_url}  out="{build_filename(e)}"' for e in entries]
    out_path = Path(path)
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_path

"""Basic LibGen search utilities."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List

import requests
from bs4 import BeautifulSoup

DEFAULT_MIRROR = "https://libgen.rs"


@dataclass
class BookEntry:
    """Represents a single LibGen search result."""

    title: str
    author: str
    year: str
    extension: str
    size: str
    md5: str
    download_url: str


def fetch_search_html(query: str, mirror: str = DEFAULT_MIRROR) -> str:
    """Return raw HTML search results for the given query."""
    params = {
        "req": query,
        "open": 0,
        "res": 50,
        "view": "simple",
        "phrase": 1,
        "column": "def",
    }
    response = requests.get(f"{mirror}/search.php", params=params, timeout=30)
    response.raise_for_status()
    return response.text


def parse_search_results(html: str) -> List[BookEntry]:
    """Parse LibGen HTML search results into a list of ``BookEntry`` objects."""
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", class_="c")
    if not table:
        return []

    entries: list[BookEntry] = []
    rows = table.find_all("tr")
    for row in rows[1:]:
        cells = row.find_all("td")
        if len(cells) < 9:
            continue
        author = cells[1].get_text(" ", strip=True)
        title = cells[2].get_text(" ", strip=True)
        year = cells[4].get_text(" ", strip=True)
        size = cells[7].get_text(" ", strip=True)
        extension = cells[8].get_text(" ", strip=True).lower()
        link_tag = cells[-1].find("a", href=True)
        download_url = link_tag["href"] if link_tag else ""
        md5_match = re.search(r"md5=([0-9a-fA-F]{32})", download_url)
        md5 = md5_match.group(1) if md5_match else ""
        entries.append(
            BookEntry(
                title=title,
                author=author,
                year=year,
                extension=extension,
                size=size,
                md5=md5,
                download_url=download_url,
            )
        )
    return entries


def search_libgen(query: str, mirror: str = DEFAULT_MIRROR) -> List[BookEntry]:
    """Search LibGen and return parsed book entries."""
    html = fetch_search_html(query, mirror)
    return parse_search_results(html)

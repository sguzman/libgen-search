"""Command-line interface for LibGen CLI."""

from __future__ import annotations

import typer

from filter import deduplicate, filter_non_books
from search import search_libgen
from urls import write_urls

app = typer.Typer(help="Search LibGen and output results")


@app.command("search")
def search_command(query: str, limit: int = 10) -> None:
    """Search LibGen for a query and print basic results."""
    entries = search_libgen(query)[:limit]
    if not entries:
        typer.echo("No results found.")
        raise typer.Exit(0)
    for idx, entry in enumerate(entries, 1):
        typer.echo(
            f"{idx}. {entry.title} - {entry.author} ({entry.year}) [{entry.extension}] {entry.size}"
        )

    choice = typer.prompt(
        "Enter comma-separated numbers to download (or 'a' for all)",
        default="a",
    )
    if choice.lower().strip() == "a":
        selected = entries
    else:
        indexes = {int(i) for i in choice.split(",") if i.strip().isdigit()}
        selected = [e for i, e in enumerate(entries, 1) if i in indexes]

    if not selected:
        typer.echo("No selections made.")
        raise typer.Exit(0)

    path = write_urls(selected)
    typer.echo(f"Wrote {len(selected)} entries to {path}")

if __name__ == "__main__":
    app()

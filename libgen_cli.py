import typer

from search import search_libgen

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


if __name__ == "__main__":
    app()

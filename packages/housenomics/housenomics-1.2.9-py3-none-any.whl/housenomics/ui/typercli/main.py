"""
CLI entry points for Typer (https://typer.tiangolo.com/) made CLI.
"""

from datetime import datetime
from importlib.metadata import version as get_version
from pathlib import Path
from typing import Optional

import typer

from housenomics.ui.typercli.adapters import (
    import_file,
    migrate_database,
    report,
    reset,
)

app = typer.Typer(
    add_completion=False,
    help="Housenomics helps you manage your personal finances.",
)


@app.command(name="version", help="Shows current version")
def version():
    typer.echo(get_version("housenomics"))


@app.command(name="import", help="Imports the transactions to feed the application")
def import_(file_path: Path):
    reset()
    migrate_database()
    import_file(file_path)


@app.command(name="report", help="Builds reports according to filters")
def report_(
    seller: Optional[str] = typer.Option(default="", help="Filters report by Seller"),
    since: Optional[datetime] = typer.Option(
        default=None, help="Show report since specified date"
    ),
    on: Optional[datetime] = typer.Option(
        default=None, help="Show report on specified date"
    ),
):
    migrate_database()
    report(seller, since, on)


@app.command(
    name="reset",
    help="Deletes all financial information from the application",
)
def reset_():
    delete_information = typer.confirm(
        "Are you sure you want to delete all financial information ?"
    )
    if not delete_information:
        raise typer.Abort()

    reset()

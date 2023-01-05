#! /usr/bin/env python3

import typer

from rich.console import Console

from sourcery_rules_generator.cli import dependencies_cli, voldemort_cli
from sourcery_rules_generator import __version__

app = typer.Typer(rich_markup_mode="markdown")
app.add_typer(dependencies_cli.app, name="dependencies")
app.add_typer(voldemort_cli.app, name="voldemort")


@app.callback(invoke_without_command=True)
def callback(
    ctx: typer.Context,
    version: bool = typer.Option(False, help="Print the current version."),
) -> None:
    """Sourcery Rules Generator"""
    if version:
        Console().print(__version__)
        return
    if ctx.invoked_subcommand is None:
        Console().print(ctx.get_help())

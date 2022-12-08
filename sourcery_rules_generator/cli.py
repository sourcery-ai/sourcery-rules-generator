#! /usr/bin/env python3

import typer
from rich.console import Console

from sourcery_rules_generator import __version__, sourcery_rules_generator

app = typer.Typer(rich_markup_mode="markdown")


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


@app.command()
def start():
    """Start a new Sourcery Rules Generator"""

    Console().print("Sourcery Rules Generator started")


@app.command()
def answer():
    """The answer to everything command"""
    result = sourcery_rules_generator.answer_everything()
    Console().print(result)

#! /usr/bin/env python3

import sys
import typer
from rich.console import Console
from rich.prompt import Prompt
from rich.syntax import Syntax

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
def create(
    package_option: str = typer.Option(
        None,
        "--package",
        help="The fully qualified name of the package",
    ),
    caller_option: str = typer.Option(
        None,
        "--importer",
        help="The fully qualified name of the allowed importer",
    ),
    interactive_flag: bool = typer.Option(
        True,
        "--interactive/--no-interactive",
        "--input/--no-input",
        help="Switch whether interactive prompts are shown. Use `--no-input` when you call this command from scripts.",
    ),
    plain: bool = typer.Option(False, help="Print only plain text."),
):
    """Create a new Sourcery dependency rule."""
    interactive = sys.stdin.isatty() and interactive_flag

    package = package_option or interactive and Prompt.ask("Package")
    allowed_importer = (
        caller_option
        or interactive
        and Prompt.ask(f"Which packages are allowed to import {package}?")
    )
    result = sourcery_rules_generator.create(package, allowed_importer)
    if plain:
        Console().print(result)
    else:
        Console().print(Syntax(result, "YAML"))

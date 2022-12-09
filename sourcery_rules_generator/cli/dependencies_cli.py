#! /usr/bin/env python3

import sys
import typer
from rich.console import Console
from rich.prompt import Prompt
from rich.syntax import Syntax

from sourcery_rules_generator import dependencies

app = typer.Typer(rich_markup_mode="markdown")


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
    result = dependencies.create_yaml_rules(package, allowed_importer)
    if plain:
        Console().print(result)
    else:
        Console().print(Syntax(result, "YAML"))

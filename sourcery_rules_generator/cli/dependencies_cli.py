#! /usr/bin/env python3

import sys
import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.syntax import Syntax

from sourcery_rules_generator import dependencies

app = typer.Typer(rich_markup_mode="markdown")


DESCRIPTION_MARKDOWN = """
# "Dependencies" Template

With the "Dependencies" template,  
you can generate rules that check which package 📦 is imported where.

For example:

* The `api` package shouldn't be imported by any other package.
* The `core` package should be imported only the `api` package.

## Parameters for the "Dependencies" Template

1. The package that gets imported. Required.
2. The package(s) that are allowed to import the package above. This parameter can be empty.
"""


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
    quiet: bool = typer.Option(
        False,
        "--quiet",
        "-q",
        help='Display less info about the "Dependencies" template.',
    ),
):
    """Create a new Sourcery dependency rule."""
    interactive = sys.stdin.isatty() and interactive_flag
    stderr_console = Console(stderr=True)
    if interactive and not quiet:
        stderr_console.print(Markdown(DESCRIPTION_MARKDOWN))
        stderr_console.rule()

    if interactive:
        stderr_console.print(Markdown('## Parameters for the "Dependencies" Template'))

    package = (
        package_option
        or interactive
        and Prompt.ask("Package (required)", console=stderr_console)
    )
    allowed_importer = (
        caller_option
        or interactive
        and Prompt.ask(
            f"Which packages are allowed to import {package}? (Leave this empty if no package is allowed to import {package}.)",
            console=stderr_console,
        )
    )
    if not package:
        _raise_error("No package provided. Can't create dependency rules.")

    result = dependencies.create_yaml_rules(package, allowed_importer)

    stderr_console.rule()
    stderr_console.print(Markdown("## Generated YAML Rules"))
    if plain:
        Console().print(result)
    else:
        Console().print(Syntax(result, "YAML"))


def _raise_error(error_msg: str, code: int = 1) -> None:
    stderr_console = Console(stderr=True, style="bold red")
    stderr_console.print(error_msg)
    raise typer.Exit(code=code)

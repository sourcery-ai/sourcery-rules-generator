#! /usr/bin/env python3

import sys
import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.syntax import Syntax

from sourcery_rules_generator import voldemort

app = typer.Typer(rich_markup_mode="markdown")


DESCRIPTION_MARKDOWN = """
# "Voldemort" Template

With the "Voldemort" template,  
you can generate rules that ensure that a specific word isn't used in your codebase.

For example:

* The word `annual` shouldn't be used, because the preferred term is `yearly`.
* The word `util` shouldn't be used, because it's overly general.

## Parameters for the "Voldemort" Template

1. The word that should be avoided. Required.
"""


@app.command()
def create(
    avoided_name_option: str = typer.Option(
        None,
        "--avoided-name",
        help="The name that should be avoided.",
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
        help='Display less info about the "Voldemort" template.',
    ),
):
    """Create a new Sourcery Voldemort rule."""
    interactive = sys.stdin.isatty() and interactive_flag
    stderr_console = Console(stderr=True)
    if interactive and not quiet:
        stderr_console.print(Markdown(DESCRIPTION_MARKDOWN))
        stderr_console.rule()

    if interactive:
        stderr_console.print(Markdown('## Parameters for the "Voldemort" Template'))

    name_to_avoid = (
        avoided_name_option
        or interactive
        and Prompt.ask("The name to avoid: (required)", console=stderr_console)
    )
    if not name_to_avoid:
        _raise_error("No name to avoid provided. Can't create voldemort rule.")

    result = voldemort.create_yaml_rules(name_to_avoid)

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

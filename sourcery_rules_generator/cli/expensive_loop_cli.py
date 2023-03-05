#! /usr/bin/env python3

import sys
import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.syntax import Syntax

from sourcery_rules_generator import expensive_loop

app = typer.Typer(rich_markup_mode="markdown")


DESCRIPTION_MARKDOWN = """
# Expensive Loop Template

With the "Expensive Loop" template,  
you can generate rules that ensure that an expensive operation isn't called in a loop.

For example:

* Call to an external API.
* Complex calculations.

## Parameters for the "Expensive Loop" Template

1. The fully qualified name of the expensive function, that you want to avoid in loops. Required.
"""


@app.command()
def create(
    avoided_function_option: str = typer.Option(
        None,
        "--avoided-function",
        help="The function that should be avoided in loops.",
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
        help='Display less info about the "Expensive Loop" template.',
    ),
):
    """Create a rule to detect an expensive call in a loop."""
    interactive = sys.stdin.isatty() and interactive_flag
    stderr_console = Console(stderr=True)
    if interactive and not quiet:
        stderr_console.print(Markdown(DESCRIPTION_MARKDOWN))
        stderr_console.rule()

    if interactive:
        stderr_console.print(
            Markdown('## Parameters for the "Expensive Loop" Template')
        )

    function_name = (
        avoided_function_option
        or interactive
        and Prompt.ask(
            "The fully qualified name of the expensive function (required)",
            console=stderr_console,
        )
    )
    if not function_name:
        _raise_error("No function name provided. Can't create Expensive Loop rule.")

    result = expensive_loop.create_yaml_rules(function_name)

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

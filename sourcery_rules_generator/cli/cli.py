#! /usr/bin/env python3

import typer

from sourcery_rules_generator.cli import dependencies

app = typer.Typer(rich_markup_mode="markdown")
app.add_typer(dependencies.app, name="dependencies")

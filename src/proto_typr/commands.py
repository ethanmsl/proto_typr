"""
Insertion point for poetry.scripts (i.e. CLI app)
"""
# import csv
# import os
# import random
# from importlib import metadata
# from typing import Optional

import typer
from rich import print as rprint

# from rich.console import Console
# from rich.errors import NotRenderableError
# from rich.table import Table

app = typer.Typer(
    add_completion=False,
)


@app.command("howdy", help="""Say hello to NAME""")
def hello(name: str) -> None:
    """
    Says "hello" to an input name.\n
    """
    rprint(f"Hello {name}")
    # example of using rich-print's MarkUp
    rprint("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")

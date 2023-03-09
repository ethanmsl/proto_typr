"""
Insertion point for poetry.scripts (i.e. CLI app)
"""
# import csv
# import os
# import random
# from importlib import metadata
# from typing import Optional

import time

import typer
from rich import print as rprint
from rich.progress import track

# from .am_camilla import i_am_camilla, am_camilla_callback

# from rich.console import Console
# from rich.errors import NotRenderableError
# from rich.table import Table
# import proto_typr.am_camilla


app = typer.Typer(
    add_completion=False,
)


@app.command("progbar")
def progress_bar_example(seconds: int = typer.Argument(5, min=1, max=16)) -> None:
    """Example of a progress bar"""

    total_so_far: int = 0
    for _ in track(range(seconds), description="Sleeping..."):
        time.sleep(1)
        total_so_far += 1
    rprint(f"Done sleeping for {total_so_far} seconds")


@app.command("nums")
def numeric_intake(
    x_int: int = typer.Argument(..., min=0, max=2),
    y_int: int = typer.Argument(..., min=-1, max=1),
) -> int:
    """testing `min` and `max` restrictions on numeric arguments"""
    print(f"X: {x_int}, Y: {y_int}")
    return x_int + y_int


def am_camilla_callback(value: str):
    """Callback for `hello` option"""
    if value != "Camilla":
        raise typer.BadParameter("Only Camilla is allowed")
    return value


@app.command("am-camilla", help="""Tell me who you are. Camilla?""")
def i_am_camilla(
    name: str = typer.Argument(..., callback=am_camilla_callback),
) -> None:
    """
    use an input callback
    """
    rprint(f"Hello {name}")
    # example of using rich-print's MarkUp
    rprint("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")


# @app.command("am-camilla", help="""Tell me who you are. Camilla?""")
# def am_camilla_command(name: str) -> None:
#     """..."""
#     i_am_camilla(name)


@app.command("howdy", help="""Say hello to NAME""")
def hello(name: str) -> None:
    """
    Says "hello" to an input name.\n
    """
    rprint(f"Hello [blue]{name}[/blue]")
    rprint("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")


@app.command()
def goodbye(name: str, formal: bool = False) -> None:
    """
    Says "goodbye" to an input name.\n
    Uses a `bool` flag to determine formality\n
    # One bars\n
    ## Two bars\n
    ### Three bars\n
    #### Four bars\n
    ##### Five bars\n
    ###### Six bars\n
    """
    if formal:
        rprint(f"Goodbye {name}. It was a pleasure.")
    else:
        rprint(f"Later {name}.")

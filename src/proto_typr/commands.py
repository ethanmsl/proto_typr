"""
Contains the bulk of top-level execution code.
However execution occurs in `__main__.py`
"""

import csv
import os
from typing import Optional

import typer
from rich import print as rprint
from rich.console import Console
from rich.table import Table

from .other_file import imma_error

app = typer.Typer(help="WHERE does THIS show UP?")

pressure_app = typer.Typer()
temperature_app = typer.Typer()
app.add_typer(pressure_app, name="pressure")
app.add_typer(temperature_app, name="temperature")


@app.command()
def hello(name: str) -> None:
    """Say hello to NAME"""
    rprint(f"Hello {name}")
    # example of using rich-print's MarkUp
    rprint("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")


@app.command()
def goodbye(name: str, formal: bool = False) -> None:
    """
    Say goodbye to `NAME`

    --formal: Use a formal goodbye
    """
    if formal:
        rprint(f"Goodbye {name}. It was a pleasure.")
    else:
        rprint(f"Later {name}.")


@app.command()
def exit_cmd_flag(code: Optional[int] = None):
    """Exit with a given code - optinonal with *flag* syntax"""
    imma_error(code)


@app.command()
def exit_cmd_opt(
    code: Optional[int] = typer.Argument(None, help="Exit with a given code")
):
    """Exit with a given code optional *argument*"""
    imma_error(code)


@app.command()
def exit_cmd_req(code: int):
    """Exit with a given code -- code is required"""
    imma_error(code)


@app.command(short_help="Run an OS command")
def oscmmd(cmd: Optional[str] = None) -> None:
    """Run the input OS Command; defaulting to to writing a test file, 'boop.txt'"""
    if cmd is None:
        cmd = r'echo "testtttting" >> boop.txt'
    rprint(os.system(cmd))


console = Console()


@app.command()
def print_rows(location: str) -> None:
    """Print rows from a file as text then as a table"""

    # first once with regular (if rich-printed) text
    with open(location, encoding="utf8") as file:
        for row in file:
            rprint(row)

    # now again using a drawn table
    with open(location, encoding="utf8") as file:
        csv_reader = csv.DictReader(file)

        header_row = list(next(csv_reader).keys())
        rprint(header_row)
        table = Table(*header_row)
        for next_row in csv_reader:
            row_list = list(next_row.values())
            rprint(row_list)
            try:
                table.add_row(*row_list)
            except ValueError:
                pass

        console.print(table)


@app.command()
def print_cwd() -> None:
    """Print the current working directory"""
    rprint(os.getcwd())


def junk_function_for_coverage_report() -> None:
    """junk function for coverage report"""
    rprint("junk")


########################################################################################
#
# @app.command()
# def delete(
#     username: str,
#     force: bool = typer.Option(
#         ...,
#         prompt="Are you sure you want to delete the user?",
#         help="Force deletion without confirmation.",
#     ),
# ):
#     """
#     Delete a user with USERNAME.
#
#     If --force is not used, will ask for confirmation.
#     """
#     if force:
#         print(f"Deleting user: {username}")
#     else:
#         print("Operation cancelled")

"""
Old scratch pad for testing out typer and rich-print
"""

import csv
import os
import random
from importlib import metadata
from typing import Optional

import typer
from rich import print as rprint
from rich.console import Console
from rich.errors import NotRenderableError
from rich.table import Table

from .other_file import imma_error

# pressure_app = typer.Typer()
# temperature_app = typer.Typer()
# app.add_typer(pressure_app, name="pressure")
# app.add_typer(temperature_app, name="temperature")

__version__ = metadata.version(__package__)


def version_callback(version: bool = typer.Option(None, "--version")):
    """Callback that returns app version"""
    if version:
        print(f"Awesome CLI Version: {__version__}")
        raise typer.Exit()


# @app.callback()
def app_callback(
    _: bool = typer.Option(None, "--version", callback=version_callback),
):
    """..."""


def hello_callback(value: str):
    """Callback for `hello` option"""
    if value != "Camila":
        raise typer.BadParameter("Only Camila is allowed")
    return value


# @app.command("howdy", help="""Say hello to NAME""")
def hello(
    name: str = typer.Argument(..., callback=hello_callback),
) -> None:
    """
    Says "hello" to an input name.\n
    Uses a callback to ensure only "Camila" is allowed.
    """
    rprint(f"Hello {name}")
    # example of using rich-print's MarkUp
    rprint("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")


# @app.command(
#     help="""
#     Say goodbye to `NAME`
#
#     --formal: Use a formal goodbye
#     """
# )


# @app.command()
def pword(
    name: str,
    password: str = typer.Option(
        ...,
        "--hidden-input-string",
        prompt=True,
        confirmation_prompt=True,
        hide_input=True,
    ),
    # NOTE: we would NOT want this as it allows explicit flag calling and regular
    #       code inputing
):
    """Example use of \"hide_input\" true."""
    print(f"Hello {name}. Doing something very secure with password.")
    print(f"...just kidding, here it is, very insecure: {password}")


##################################################
# @app.command(rich_help_panel="exits")
def exit_cmd_flag(
    code: Optional[int] = typer.Option(
        None,
        "--exit-code",
        "-c",
        help="Code to exit with.",
        prompt="Please enter an exit code.",
        confirmation_prompt=True,
    )
):
    """Exit with a given code - will prompt for code if forgotten"""
    imma_error(code)


# @app.command(rich_help_panel="exits")
def exit_cmd_opt(
    code: Optional[int] = typer.Argument(
        None,
        help="Code to exit with.",
        show_default="Special: aborted.",
        metavar="exit_code",
        rich_help_panel="Example Panel",
    )
):
    """Exit with a given code optional *argument*"""
    imma_error(code)


# @app.command(rich_help_panel="exits")
def exit_cmd_req(code: int):
    """Exit with a given code -- code is required"""
    imma_error(code)


#######################################################
def get_name():
    """Returns a random str from a list"""
    return random.choice(["Deadpool", "Rick", "Morty", "Hiro"])


# @app.command()
def rand_default(
    name: str = typer.Argument(
        get_name, help="The name to greet. Can be chosen at random."
    )
):
    """Demonstrates using a function to generate default"""
    print(f"Hello {name}")


########################################################


# @app.command(short_help="Run an OS command")
def oscmmd(cmd: Optional[str] = None) -> None:
    """Run the input OS Command; defaulting to to writing a test file, 'boop.txt'"""
    if cmd is None:
        cmd = r'echo "testtttting" >> boop.txt'
    rprint(os.system(cmd))


console = Console()


# @app.command()
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
            except NotRenderableError:
                pass

        console.print(table)


# @app.command()
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

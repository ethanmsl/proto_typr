"""
Insertion point for poetry.scripts (i.e. CLI app)
"""
# import csv
# import os
# import random
# from importlib import metadata
# from typing import Optional

import time
from pathlib import Path

import typer
from rich import print as rprint
from rich.progress import Progress, SpinnerColumn, TextColumn, track

# from .am_camilla import i_am_camilla, am_camilla_callback

# from rich.console import Console
# from rich.errors import NotRenderableError
# from rich.table import Table
# import proto_typr.am_camilla


app = typer.Typer(
    add_completion=False,
)

APP_NAME = "proto-typr"


@app.command("config_write")
def config_find_and_write(to_write: str) -> None:
    """trying to write to a hypothetical config file"""
    rprint(f"not doing anything wiht this currently {to_write}")
    app_dir = typer.get_app_dir(APP_NAME)
    app_dir_path = Path(app_dir)
    app_dir_path.mkdir(parents=True, exist_ok=True)
    config_path: Path = Path(app_dir) / "config.json"
    if not config_path.is_file():
        config_path.write_text('{"version": "1.0.0"}')
    config_file_str = str(config_path)
    print("Opening config directory")
    typer.launch(config_file_str, locate=True)


@app.command("app_dir")
def get_app_dir() -> None:
    """Get the app directory"""
    app_dir = typer.get_app_dir(APP_NAME)
    config_path: Path = Path(app_dir) / "config.json"
    rprint(
        f"\nusing non-typer methods:\nApp directory: {Path(__file__).parent.absolute()}"
    )
    rprint("\nusing typer methods: ...")
    if not config_path.is_file():
        rprint(f"Config file not found at {config_path}")
        raise typer.Abort()
    rprint(f"App directory: {config_path}")


@app.command("spin")
def spinner_example(seconds: int = typer.Argument(5, min=1, max=36)) -> None:
    """Example of a progress bar"""

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}", justify="right"),
        transient=True,
    ) as progress:
        progress.add_task("Task A...", total=seconds)
        task = progress.add_task("Task B...", total=seconds)
        for _ in range(seconds):
            time.sleep(1)
            progress.advance(task)


@app.command("progbar")
def progress_bar_example(
    seconds: int = typer.Argument(5, min=1, max=16), plain_bar: bool = False
) -> None:
    """
    Example of a progress bar.
    Default uses Rich. (colorful, but simple)
    Use `--plain-bar` to use Typer's progress bar.
    Which actually has a very nice, minimalist ascii aesthetic.
    """

    if not plain_bar:
        total_so_far: int = 0
        for _ in track(range(seconds), description="Sleeping..."):
            time.sleep(1)
            total_so_far += 1
        rprint(f"Done sleeping for {total_so_far} seconds")
    else:
        total_so_far_2 = 0
        with typer.progressbar(range(seconds), label="Sleeping...") as progress:
            for _ in progress:
                time.sleep(1)
                total_so_far_2 += 1
        rprint(f"Done sleeping for {total_so_far_2} seconds")


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

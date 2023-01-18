"""
Contains the bulk of top-level execution code.
However execution occurs in `__main__.py`
"""

import os

import typer

app = typer.Typer()


@app.command()
def hello(name: str) -> None:
    """Say hello to NAME"""
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False) -> None:
    """
    Say goodbye to `NAME`

    --formal: Use a formal goodbye
    """
    if formal:
        print(f"Goodbye {name}. It was a pleasure.")
    else:
        print(f"Later {name}.")


@app.command()
def print_rows(location: str) -> None:
    """Print rows from a file"""
    with open(location, encoding="utf8") as file:
        for row in file:
            print(row)


@app.command()
def print_cwd() -> None:
    """Print the current working directory"""
    print(os.getcwd())


def junk_function_for_coverage_report() -> None:
    """junk function for coverage report"""
    print("junk")

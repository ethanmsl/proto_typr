"""
Contains the bulk of top-level execution code.
However execution occurs in `__main__.py`
"""

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


def junk_function_for_coverage_report() -> None:
    """junk function for coverage report"""
    print("junk")

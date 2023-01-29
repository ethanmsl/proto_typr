"""
just to test linking files using typer
"""


from typing import Optional
import typer


def imma_error(code: Optional[int]):
    """this raises aa typer exception with an errorcode"""
    if code is None:
        raise typer.Abort()  # prints "Aborted." to console
    raise typer.Exit(code=code)

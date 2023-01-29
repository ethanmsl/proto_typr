"""
just to test linking files using typer
"""


import typer


def imma_error(code: int):
    """this raises aa typer exception with an errorcode"""
    raise typer.Exit(code=code)

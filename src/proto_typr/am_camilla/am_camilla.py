"""
Function and callback for asserting that you are "Camilla"
"""

import typer
from rich import print as rprint


def am_camilla_callback(value: str):
    """Callback for `hello` option"""
    if value != "Camila":
        raise typer.BadParameter("Only Camila is allowed")
    return value


def i_am_camilla(
    name: str = typer.Argument(..., callback=am_camilla_callback),
) -> None:
    """
    use an input callback
    """
    rprint(f"Hello {name}")
    # example of using rich-print's MarkUp
    rprint("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")

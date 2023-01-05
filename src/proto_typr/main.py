"""
Contains the bulk of top-level execution code.
However execution occurs in `__main__.py`
"""

# import typer


def main(name: str) -> None:
    """primary execution function"""
    print(f"Hello {name}")


def junk_function_for_coverage_report() -> None:
    """junk function for coverage report"""
    print("junk")

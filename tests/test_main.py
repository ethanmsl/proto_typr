"""
Tests for `commands.py`
"""

from proto_typr import commands


def test_app() -> None:
    """Test: Test the `app()`
    This is not a reasonable test and being skipped.
    """
    assert True


def test_hello() -> None:
    """Test: Say hello to NAME"""
    assert commands.hello("gloomba") is None


def test_goodbye() -> None:
    """Test:Say goodbye to NAME"""
    assert commands.goodbye("gloomba") is None
    assert commands.goodbye("gloombs", False) is None
    assert commands.goodbye("Madam Gloomba", True) is None


def test_print_rows() -> None:
    """Print rows from a file"""
    location: str = "inclusion_dir/some_rows.csv"
    assert commands.print_rows(location) is None


def test_print_cwd() -> None:
    """Print the current working directory"""
    assert commands.print_cwd() is None


def test_junk_function_for_coverage_report() -> None:
    """test of junk function for coverage report"""
    assert commands.junk_function_for_coverage_report() is None

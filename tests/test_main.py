"""
Tests for `main.py`
"""

from proto_typr import main


def test_app() -> None:
    """Test: Test the `app()`
    This is not a reasonable test and being skipped.
    """
    assert True


def test_hello() -> None:
    """Test: Say hello to NAME"""
    assert main.hello("gloomba") is None


def test_goodbye() -> None:
    """Test:Say goodbye to NAME"""
    assert main.goodbye("gloomba") is None
    assert main.goodbye("gloombs", False) is None
    assert main.goodbye("Madam Gloomba", True) is None


def test_print_rows() -> None:
    """Print rows from a file"""
    location: str = "inclusion_dir/some_rows.csv"
    assert main.print_rows(location) is None


def test_print_cwd() -> None:
    """Print the current working directory"""
    assert main.print_cwd() is None


def test_junk_function_for_coverage_report() -> None:
    """test of junk function for coverage report"""
    assert main.junk_function_for_coverage_report() is None

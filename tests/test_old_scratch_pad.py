"""
Tests for `old_scratch_pad.py`
"""

from proto_typr import old_scratch_pad


def test_app() -> None:
    """Test: Test the `app()`
    This is not a reasonable test and being skipped.
    """
    assert True


def test_hello() -> None:
    """Test: Say hello to NAME"""
    assert old_scratch_pad.hello("gloomba") is None


def test_goodbye() -> None:
    """Test:Say goodbye to NAME"""
    assert old_scratch_pad.goodbye("gloomba") is None
    assert old_scratch_pad.goodbye("gloombs", False) is None
    assert old_scratch_pad.goodbye("Madam Gloomba", True) is None


def test_print_rows() -> None:
    """Print rows from a file"""
    location: str = "inclusion_dir/some_rows.csv"
    assert old_scratch_pad.print_rows(location) is None


def test_print_cwd() -> None:
    """Print the current working directory"""
    assert old_scratch_pad.print_cwd() is None


def test_junk_function_for_coverage_report() -> None:
    """test of junk function for coverage report"""
    assert old_scratch_pad.junk_function_for_coverage_report() is None

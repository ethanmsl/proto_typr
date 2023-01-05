"""
Tests for `main.py`
"""

from proto_typr import main


def test_main() -> None:
    """trivially true for the time being"""
    assert main.main("aname") is None


def test_junk_function_for_coverage_report() -> None:
    """test of junk function for coverage report"""
    assert main.junk_function_for_coverage_report() is None

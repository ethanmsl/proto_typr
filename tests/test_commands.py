"""
Unit tests for `commands.py`
"""

from proto_typr import commands


def test_hello() -> None:
    """Test: Say hello to NAME"""
    assert commands.hello("gloomba") is None


def test_goodbye() -> None:
    """Test:Say goodbye to NAME"""
    assert commands.goodbye("gloomba") is None
    assert commands.goodbye("gloombs", False) is None
    assert commands.goodbye("Madam Gloomba", True) is None

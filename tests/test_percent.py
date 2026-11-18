import pytest

from src import calc, strutils


def test_percent():  # TST-7
    assert calc.percent(1, 4) == 25.0


def test_percent_of_zero():  # TST-7
    with pytest.raises(ValueError):
        calc.percent(1, 0)


def test_format_percent():  # TST-7
    assert strutils.format_percent(25.0) == "25%"
    assert strutils.format_percent(33.333) == "33.3%"

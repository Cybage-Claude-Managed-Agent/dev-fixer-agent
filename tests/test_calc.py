import pytest

from src.calc import add, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5


def test_add_negative():  # TST-1
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_divide_places():  # TST-6
    assert divide(10, 3, places=2) == 3.33
    assert divide(10, 4) == 2.5
    with pytest.raises(ValueError):
        divide(1, 0, places=2)

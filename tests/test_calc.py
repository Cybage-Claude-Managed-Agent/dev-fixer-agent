import pytest

from src.calc import add, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),
        (10, 20, 30),
        (-2, -3, -5),
        (-7, 4, -3),
        (7, -4, 3),
        (0, 5, 5),
        (0, -5, -5),
        (0.1, 0.2, 0.3),
        (-1.5, 2.25, 0.75),
    ],
)
def test_add_regression(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a, b", [(2, 3), (-4, 9), (1.5, -0.25)])
def test_add_commutative(a, b):
    assert add(a, b) == pytest.approx(add(b, a))

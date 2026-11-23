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
    ("a", "b", "expected"),
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (-2, -3, -5),
        (0, 7, 7),
        (7, 0, 7),
        (10, 4, 14),
        (2.5, 0.5, 3.0),
    ],
)
def test_add_parametrized(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


def test_add_is_commutative():
    assert add(3, 10) == add(10, 3) == 13

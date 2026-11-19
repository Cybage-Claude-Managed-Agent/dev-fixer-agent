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
    [(2, 3, 5), (-2, 3, 1), (0, 0, 0), (-4, -6, -10)],
)
def test_add_regression_scrum_9(a: float, b: float, expected: float) -> None:
    assert add(a, b) == expected

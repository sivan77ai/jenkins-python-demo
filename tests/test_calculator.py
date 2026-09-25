"""Tests for the calculator module."""

import pytest

from src.calculator import add, subtract, multiply, divide, average


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-4, 1) == -3


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 7) == 21


def test_divide():
    assert divide(9, 3) == 3


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(5, 0)


def test_average():
    assert average([2, 4, 6]) == 4


def test_average_empty_raises():
    with pytest.raises(ValueError):
        average([])


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, 0),
        (1, 1, 2),
        (100, 250, 350),
        (-5, 5, 0),
    ],
)
def test_add_many_cases(a, b, expected):
    assert add(a, b) == expected

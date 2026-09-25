"""A tiny calculator module used to practise CI with Jenkins."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b.

    Raises:
        ValueError: if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def average(numbers):
    """Return the mean of a non-empty list of numbers.

    Raises:
        ValueError: if the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot average an empty list")
    return sum(numbers) / len(numbers)

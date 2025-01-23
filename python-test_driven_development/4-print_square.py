#!/usr/bin/python3
"""
This module provides the `print_square` function.

The `print_square` function prints a square with the character '#',
where the size of the square is specified as an integer parameter.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or a float equivalent toaninteger.
        ValueError: If size is less than 0.
    """
    # Handle floats that are equivalent to integers
    if isinstance(size, float) and size.is_integer():
        size = int(size)
    # Check if size is an integer
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")
    # Print the square
    for _ in range(size):
        print("#" * size)

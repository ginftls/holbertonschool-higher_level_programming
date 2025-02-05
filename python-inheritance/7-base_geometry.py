#!/usr/bin/python3
"""
This module defines a BaseGeometry class with methods to validate integers
and compute area (not yet implemented).
"""


class BaseGeometry:
    """
    A base class for geometry-related operations.
    """

    def area(self):
        """
        Raises an Exception indicating that the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a given value is a positive integer.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

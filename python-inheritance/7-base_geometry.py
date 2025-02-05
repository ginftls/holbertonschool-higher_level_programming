#!/usr/bin/python3
"""Defines a class BaseGeometry with area and integer_validator methods."""


class BaseGeometry:
    """A class representing basic geometry operations."""

    def area(self):
        """Raises an Exception indicating that area() is not implemented.

        Raises:
            Exception: Always raises an exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value.

        Args:
            name (str): The name of the value (assumed to always be a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

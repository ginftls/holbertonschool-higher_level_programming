#!/usr/bin/python3
"""Defines a class BaseGeometry with a public instance method area."""


class BaseGeometry:
    """A class representing basic geometry operations."""

    def area(self):
        """Raises an Exception indicating that area() is not implemented.

        Raises:
            Exception: Always raises an exception with the message
            'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

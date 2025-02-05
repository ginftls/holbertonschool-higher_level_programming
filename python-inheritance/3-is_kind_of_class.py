#!/usr/bin/python3
"""
Module that provides a function to check if an object
is an instance of, or if the object is an instance of a class
that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of, or if obj is an instance
    of a class that inherited from, a_class. Otherwise, returns False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

        Returns:
        bool:True if obj is an instance of or inherits from a_class,False
        otherwise.
    """
    return isinstance(obj, a_class)

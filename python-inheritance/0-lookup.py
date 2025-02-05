#!/usr/bin/python3
"""
Module for lookup function that return list of available attributes and methods
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

        Args:
        obj: The object to inspect

    Returns:
        list: List of attributes and methods of the object
    """
    return dir(obj)

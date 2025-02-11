#!/usr/bin/python3
"""
Module for class_to_json function.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary representation of obj.
    """
    return obj.__dict__

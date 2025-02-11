#!/usr/bin/python3

"""
Module that provides a function to create an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Reads a JSON file and returns the corresponding Python object.

       Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        object: The Python object parsed from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

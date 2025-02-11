#!/usr/bin/python3


"""
Module 5-save_to_json_file
This module contains a function
that writes an Object to a text file,
using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: The object to be serialized and written to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)

#!/usr/bin/python3
"""
Module 5-text_indentation
Defines afunction that prints a text with 2 new lines after certain characters.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:'.', '?',':'.

    Args:
        text (str): The text to be formatted and printed.

    Raises:
        TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define the characters after which to add new lines
    triggers = ['.', '?', ':']
    i = 0

    while i < len(text):
        print(text[i], end="")
        if text[i] in triggers:
            print("\n")
            # Skip following spaces
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

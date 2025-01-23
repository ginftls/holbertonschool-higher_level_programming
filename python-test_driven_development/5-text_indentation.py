#!/usr/bin/python3
"""
Module 5-text_indentation
Defines a function that prints a text with 2 new lines after certaincharacters
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines aftereach of thesecharacters: '.', '?', ':'.

    Args:
        text (str): The text to be formatted and printed.

    Raises:
        TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove leading/trailing spaces and initialize variables
    text = text.strip()
    triggers = ['.', '?', ':']
    formatted_text = ""
    i = 0

    while i < len(text):
        formatted_text += text[i]
        if text[i] in triggers:
            formatted_text += "\n\n"  # Add two new lines after triggers
            i += 1
            # Skip spaces after triggers
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    print(formatted_text, end="")

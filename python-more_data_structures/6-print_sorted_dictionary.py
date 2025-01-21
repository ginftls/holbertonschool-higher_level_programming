#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary with keys sorted in alphabetical order."""
    # Sort the keys of the dictionary and iterate over them
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")

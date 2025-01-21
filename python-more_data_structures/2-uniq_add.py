#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)."""
    # Use a set to remove duplicates and sum the unique elements
    return sum(set(my_list))

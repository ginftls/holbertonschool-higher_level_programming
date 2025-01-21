#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of search with replace in a new list."""
    # Use a list comprehension to create a new list with the replaced elements
    return [replace if element == search else element for element in my_list]

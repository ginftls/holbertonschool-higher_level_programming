#!/usr/bin/python3
"""
Module containing MyList class that inherits from list
"""


class MyList(list):
    """
    A class that inherits from list and adds a print_sorted method
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        All elements are assumed to be of type int
        """
        print(sorted(self))

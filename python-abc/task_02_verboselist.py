#!/usr/bin/python3
"""Extending the Python List with Notifications"""


class VerboseList(list):
    """VerboseList class"""
    def append(self, item):
        """to add item to the list"""
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, items):
        """to print the numbers of items"""
        print("Extended the list with [{}] items.".format(len(items)))
        super().extend(items)

    def remove(self, item):
        """to remove item from the list"""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """to remove an index from the list"""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)

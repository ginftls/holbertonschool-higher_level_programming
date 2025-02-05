#!/usr/bin/python3

def inherits_from(obj, a_class):
    """Check if obj is an instance of a class inheriting from a_class."""
    if not isinstance(a_class, type):
        return False
    return issubclass(type(obj), a_class) and (type(obj) is not a_class)

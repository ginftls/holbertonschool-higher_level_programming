#!/usr/bin/python3
""" Module for the inherits_from method """


def inherits_from(obj, a_class):

    return issubclass(type(obj), a_class) and type(obj) is not a_class

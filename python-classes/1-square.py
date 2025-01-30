#!/usr/bin/python3
""" Class Square that defines a square """


class Square:
    """ Class Square """
    __size = None

    def __init__(self, size=__size):
        if size is not None:
            self.__size = size

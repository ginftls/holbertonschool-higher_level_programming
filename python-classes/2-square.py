#!/usr/bin/python3
class Square:
    """
    Square class. Class is used to create square of given size.

    Attributes:
        __size (int): Size of square, defaults to 0.
    """

    def __init__(self, size=0):
        """
        Constructor of Square class.

        Args:
            size (int, optional): Size of square to be created. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):  # Check if size is an integer.
            raise TypeError("size must be an integer")
        if size < 0:  # Check if size is greater than or equal to 0.
            raise ValueError("size must be >= 0")
        self.__size = size  # Set size of square.
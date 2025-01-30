#!/usr/bin/python3
class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """
        Initializes the square with a private instance attribute size.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
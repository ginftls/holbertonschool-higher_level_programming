#!/usr/bin/python3
from rectangle import Rectangle

class Square(Rectangle):
    """
    A class that represents a square, which is a subclass of Rectangle.
    """

    def __init__(self, size):
        """
        Initializes the square with the given size.
        
        Args:
            size (int): The size of the square (must be a positive integer).
        """
        self.integer_validator("size", size)  # Validate size using the parent method
        self._size = size  # Private variable to store size

        # Initialize the parent Rectangle class with width and height equal to size
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self._size * self._size  # Area of a square is side^2

    def __str__(self):
        """
        Returns a string representation of the square.
        
        Returns:
            str: A string in the format [Square] <width>/<height>.
        """
        return f"[Square] {self._size}/{self._size}"

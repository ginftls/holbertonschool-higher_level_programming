#!/usr/bin/python3


def __init__(self, width, height):
    """Initialize a Rectangle instance with validated width and height."""
    super().__init__()
    self.__width = width
    self.__height = height
    self.integer_validator("width", self.__width)
    self.integer_validator("height", self.__height)


def area(self):
    """Calculate and return the area of the rectangle."""
    return self.__width * self.__height


def __str__(self):
    """Return a string representation of the rectangle."""
    return f"[Rectangle] {self.__width}/{self.__height}"

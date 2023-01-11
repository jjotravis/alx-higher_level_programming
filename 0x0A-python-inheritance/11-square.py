#!/usr/bin/python3
"""Defines a class that inherits from class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square from a Rectangle"""

    def __init__(self, size):
        """Initializes a new instance of a square
        Args:
            size: The length and(or) height of square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Magic methpd to print square description"""

        return ("[Square] {}/{}".format(self.__size, self.__size))

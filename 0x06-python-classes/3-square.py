#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Representation of square"""

    def __init__(self, size=0):
        """Initialize a new square"""
        if not isinstance(size, int):
            raise TypeError
        elif size < 0:
            raise ValueError
        self.__size = size

    def area(self):
        """Get the area of the square"""
        return (self.__size * self.__size)

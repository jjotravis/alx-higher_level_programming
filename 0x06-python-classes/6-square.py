#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Representation of square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set required value for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """set position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num > 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Get the area of the square"""
        return (self.size * self.size)

    def my_print(self):
        """prints the square"""
        if (self.size) == 0:
            print("")
            return

        [print("") for i in range(self.position[1])]
        for i in range(self.size):
            [print("", end="") for j in range(self.position[0])]
            [print("#", end="") for k in range(self.size)]
            print()

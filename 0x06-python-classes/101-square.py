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
        message = 'position must be a tuple of 2 positive integers'
        if type(value) != tuple or len(value) != 2:
            raise TypeError(message)

        for items in value:
            if type(items) != int or items < 0:
                raise TypeError(message)
        self.__position = value

    def area(self):
        """Get the area of the square"""
        return (self.size * self.size)

    def my_print(self):
        """prints the square"""
        if (self.size) == 0:
            print()
            return

        [print() for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print()

    def __str__(self):
        """Print representation of a square"""
        if self.__size != 0:
            [print() for i in range(self.__position[1])]
        for i in range(self.__size):
            [print("_", end="") for j in range(self.__position[0])]
            [print('#', end="") for k in range(self.__size)]
            if i != self.__size - 1:
                print("")
        return("")

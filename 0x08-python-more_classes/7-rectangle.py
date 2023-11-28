#!/usr/bin/python3
"""Define a class rectangle"""


class Rectangle:
    """Representation of a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set required type for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set required type value for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Gives the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Gives the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)

    def __str__(self):
        """Print() __str__ method function to return in char #"""

        res = ""
        if self.__height == 0 or self.__width == 0:
            return res

        for i in range(self.__height):
            if i == self.__height - 1:
                res += (str(self.print_symbol) * self.__width)
            else:
                res += ((str(self.print_symbol) * self.__width) + '\n')

        return res

    def __repr__(self):
        """print() or eval() __repr__ method function to return
        ...Rectangle(width, height)
        """
        w = str(self.__width)
        h = str(self.__height)

        res = "Rectangle(" + w + ", " + h + ")"
        return res

    def __del__(self):
        """Print message for delete"""
        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")

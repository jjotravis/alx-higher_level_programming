#!/usr/bin/python3
"""Class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Class definitions and instances"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes an instance of rectangle
        Args:
            width (int): Width of the rectangle
            height (int): Height of rectangle
            x (int): x coordinate of new Rectangle
            y (int): y coordinate of new Rectangle
            id (int): the id of new rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getting valueof width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Get right type for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getting value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Get right type for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getting value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Getting right type for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getting value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Getting right type for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of Rectangle"""
        return self.width * self.height

    def display(self):
        """Prints instance of rectangle to stdout"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print() for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print()

    def update(self, *args, **kwargs):
        """Update the Rectangle

        Args:
            *args (int): New attribute values
                - 1st argument rep id
                - 2nd argument rep width
                - 3rd argument rep height
                - 4th argument rep x
                - 5th argument rep y
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionaary representation of rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return print() and str() representation of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

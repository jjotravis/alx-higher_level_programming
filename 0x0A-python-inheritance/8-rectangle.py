#!/usr/bin/python3
"""A class BaseGeometry for geometry module"""


class BaseGeometry:
    """The class defining geometry module"""
    def area(self):
        """raises an excpetion"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value is an int"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """class inheriting from BaseGeometry"""
    def __init__(self, width, height):
        """initializes an instance of Rectangle"""
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

        self.__width = width
        self.__height = height

#!/usr/bin/python3
"""Defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square

        Args:
            size (int): The size of the new square
            x (int): x coordinate of the new square
            y (int): y coordinate of the new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size of Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Defines size value"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns print() and str() representantion of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

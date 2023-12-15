
#!/usr/bin/python3

import unittest
import os
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    # Creating a new instance of Rectangle with valid arguments sets the attributes correctly
    def test_valid_arguments(self):
        rectangle = Rectangle(5, 10, 1, 2, 3)
        assert rectangle.width == 5
        assert rectangle.height == 10
        assert rectangle.x == 1
        assert rectangle.y == 2
        assert rectangle.id == 3

    # Calling area() on a Rectangle instance returns the correct area
    def test_area(self):
        rectangle = Rectangle(5, 10)
        assert rectangle.area() == 50

    # Calling display() on a Rectangle instance prints the correct representation to stdout
    def test_display(self, capsys):
        rectangle = Rectangle(5, 3)
        rectangle.display()
        captured = capsys.readouterr()
        assert captured.out == "#####\n#####\n#####\n"

    # Creating a new instance of Rectangle with a width or height of 0 raises a ValueError
    def test_zero_width_height(self):
        with unittest.raises(ValueError):
            Rectangle(0, 5)
        with unittest.raises(ValueError):
            Rectangle(5, 0)

    # Creating a new instance of Rectangle with a negative x or y value raises a ValueError
    def test_negative_x_y(self):
        with unittest.raises(ValueError):
            Rectangle(5, 10, -1, 2)
        with unittest.raises(ValueError):
            Rectangle(5, 10, 1, -2)

    # Creating a new instance of Rectangle with a non-integer width or height value raises a TypeError
    def test_non_integer_width_height(self):
        with unittest.raises(TypeError):
            Rectangle(5.5, 10)
        with unittest.raises(TypeError):
            Rectangle(5, "10")
#!/usr/bin/python3
import os
import unittest
from models.rectangle import Rectangle

class TestToDictionary(unittest.TestCase):

    # Returns a dictionary with keys "id", "width", "height", "x", and "y"
    def test_returns_dictionary_with_keys(self):
        rectangle = Rectangle(10, 20, 5, 5, 1)
        dictionary = rectangle.to_dictionary()
        assert isinstance(dictionary, dict)
        assert "id" in dictionary
        assert "width" in dictionary
        assert "height" in dictionary
        assert "x" in dictionary
        assert "y" in dictionary

    # The values of the dictionary match the attributes of the Rectangle instance
    def test_values_match_attributes(self):
        rectangle = Rectangle(10, 20, 5, 5, 1)
        dictionary = rectangle.to_dictionary()
        assert dictionary["id"] == rectangle.id
        assert dictionary["width"] == rectangle.width
        assert dictionary["height"] == rectangle.height
        assert dictionary["x"] == rectangle.x
        assert dictionary["y"] == rectangle.y

    # The dictionary is returned without errors
    def test_returns_dictionary_without_errors(self):
        rectangle = Rectangle(10, 20, 5, 5, 1)
        try:
            dictionary = rectangle.to_dictionary()
        except Exception as e:
            unittest.fail(f"Unexpected exception: {e}")

    # The Rectangle instance has minimum values for width and height (1)
    def test_minimum_width_and_height(self):
        rectangle = Rectangle(1, 1, 0, 0, 1)
        dictionary = rectangle.to_dictionary()
        assert dictionary["width"] == 1
        assert dictionary["height"] == 1

    # The Rectangle instance has maximum values for width and height (1000000)
    def test_maximum_width_and_height(self):
        rectangle = Rectangle(1000000, 1000000, 0, 0, 1)
        dictionary = rectangle.to_dictionary()
        assert dictionary["width"] == 1000000
        assert dictionary["height"] == 1000000

    # The Rectangle instance has minimum values for x and y (0)
    def test_minimum_x_and_y(self):
        rectangle = Rectangle(10, 20, 0, 0, 1)
        dictionary = rectangle.to_dictionary()
        assert dictionary["x"] == 0
        assert dictionary["y"] == 0

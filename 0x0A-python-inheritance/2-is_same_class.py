#!/usr/bin/python3
"""Checks if an obect is an instance of a specified class"""


def is_same_class(obj, a_class):
    """
    Function to check if an object is an instance of a class
    Args:
        obj - object
        a_class - instance to check
    Return: True if is an instance false otherwise
    """
    if (type(obj) == a_class):
        return True
    else:
        return False

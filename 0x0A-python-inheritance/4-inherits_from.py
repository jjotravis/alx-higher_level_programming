#!/usr/bin/python3
"""Checks if object is class that it inherited"""


def inherits_from(obj, a_class):
    """
    function for direct or indirect inheritance from class
    Args:
        obj: object to check
        a_class: specified class
    Return: True if function passes false otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

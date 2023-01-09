#!/usr/bin/python3
"""Checks if object is an instance of class"""


def is_kind_of_class(obj, a_class):
    """
    if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class

    Args:
        obj: obect to check
        a_class: class instance
    Returns: True or False
    """
    return (isinstance(obj, a_class))

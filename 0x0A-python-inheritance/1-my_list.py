#!/usr/bin/python3
""" Subclass of list"""


class MyList(list):
    """Class that inherits from list"""

    def __init__(self):
        """initialize the object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))

#!/usr/bin/python3
"""Module for printing a square with"""


def print_square(size):
    """Define funtion to print square with # character

    Args:
        size (int): length of square
    Raises:
        ValueError: when size is < 0
        TypeError: when size is a float and < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="")for j in range(size)]
        print()

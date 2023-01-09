#!/usr/bin/python3
"""Module to prinr available attributes and ethods of an object"""


def lookup(obj):
    """Returns list of available attributes and methods for object"""
    return (dir(obj))

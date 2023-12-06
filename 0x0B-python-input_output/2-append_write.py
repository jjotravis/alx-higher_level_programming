#!/usr/bin/python3
"""Appends text to a file"""


def append_write(filename="", text=""):
    """Appends a string to end of a UFT8 file
    returns number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

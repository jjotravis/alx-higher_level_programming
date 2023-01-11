#!/usr/bin/python3
"""Write a string to text file"""


def write_file(filename="", text=""):
    """Writes to a UTF8 textfile and returnd number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

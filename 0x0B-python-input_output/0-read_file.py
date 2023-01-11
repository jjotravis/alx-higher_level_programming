#!/usr/bin/python3
"""reads a text file and prints to std out"""


def read_file(filename=""):
    """Prints the contents of a a utf8 text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """Function that prints 2 new line after
    . or ? or : in text
    Raises:
        TypeError: when text is not a string
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
                c += 1
        c += 1

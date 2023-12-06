#!/usr/bin/python3
"""Writes object to a text file using JSON"""


def save_to_json_file(my_obj, filename):
    """
    Function that writes to a textfile
    Args:
        my_obj: Object to be written
        filename: destination text file
    """
    import json
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)

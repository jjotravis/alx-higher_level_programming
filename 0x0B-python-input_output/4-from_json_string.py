#!/usr/bin/python3
"""Returns an object with JSON representation"""


def from_json_string(my_str):
    """Function that does conversion"""
    import json
    return json.loads(my_str)

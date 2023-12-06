#!/usr/bin/python3
"""Function to get Json representation of an object"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object"""
    import json
    return json.dumps(my_obj)

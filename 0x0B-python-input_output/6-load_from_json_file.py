#!/usr/bin/python3
"""Creates an obect from JSON file"""
import json


def load_from_json_file(filename):
    """Function that creates Object"""
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)

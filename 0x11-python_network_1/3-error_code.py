#!/usr/bin/python3
"""Sends request to URL
Displays body of response
Handle HTTPError

Usage: ./3-error_code.py <URL>
"""
import sys
import urllib.request
from urllib.error import HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: ", e.code)

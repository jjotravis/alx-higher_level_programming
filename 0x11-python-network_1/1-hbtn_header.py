#!/usr/bin/python3
"""Sends a request to URL
Displays value of X-Request-Id

Usage: ./1-hbtn_header.py <url>
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))

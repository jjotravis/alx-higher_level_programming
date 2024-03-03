#!/usr/bin/python3
"""Sends a request to URL
Displays value of X-Request-Id
use requests

Usage: ./5-hbtn_header.py <url>
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request = requests.get(url)
    print(request.headers.get("X-Request-Id"))

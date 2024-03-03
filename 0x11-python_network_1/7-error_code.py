#!/usr/bin/python3
"""Sends request to URL
Displays body of response
Handle HTTPError

Usage: ./7-error_code.py <URL>
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    status = req.status_code
    if status < 400:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))

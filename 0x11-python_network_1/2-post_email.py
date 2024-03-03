#!/usr/bin/python3
"""Takes in a URL and an email, 
sends a POST request to  URL with the email as a parameter
displays the body of the response

Usage: ./2-post_email.py <URL> <email>
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(value).encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))

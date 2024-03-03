#!/usr/bin/python3
"""Takes in a URL and an email, 
sends a POST request to  URL with the email as a parameter
displays the body of the response

Usage: ./6-post_email.py <URL> <email>
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    req = requests.post(url, data=value)
    print(req.text)

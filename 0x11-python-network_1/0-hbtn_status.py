#!/usr/bin/python3
"""Script that fetches given url
url: 'https://alx-intranet.hbtn.io/status'
uses urllib
"""

import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    response = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
    print("\t- utf8 content: {}".format(response.decode(encoding="utf8")))

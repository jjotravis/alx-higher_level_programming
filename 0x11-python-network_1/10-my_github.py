#!/usr/bin/python3
"""takes your GitHub credentials
 uses the GitHub API to display your id

 Usage: ./10-my_github.py <user> <tokens>
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

user = sys.argv[1]
psswd = sys.argv[2]
auth = HTTPBasicAuth(user, psswd)

req = requests.get("https://api.github.com/user", auth=auth)
print(req.json().get("id"))

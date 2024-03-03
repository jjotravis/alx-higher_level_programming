#!/usr/bin/python3
"""
 takes in a letter as parameter in var q
 sends a POST request to http://0.0.0.0:5000/search_user.

 Usage: ./8-json_api.py q
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    value = {"q": letter}
    r = requests.post("http://0.0.0.0:5000/search_user", data=value)

    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")

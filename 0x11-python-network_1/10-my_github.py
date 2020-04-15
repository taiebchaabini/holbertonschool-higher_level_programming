#!/usr/bin/python3
import requests
import sys
"""
Python script that takes your Github credentials (username and password) and
uses the Github API to display your id
"""
if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    token = sys.argv[2]
    logins = (username, token)
    r = requests.get(url, auth=logins)
    try:
        print(r.json()['id'])
    except:
        print("None")

#!/usr/bin/python3
import requests
import sys
"""
Python script that takes in a URL and an email address, sends a POST request to
the passed URL with the email as a parameter, and finally displays the body of
the response.
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

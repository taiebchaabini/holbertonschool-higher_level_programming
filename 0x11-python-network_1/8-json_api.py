#!/usr/bin/python3
import requests
import sys
"""
Python script that takes in a URL and an email address, sends a POST request to
the passed URL with the email as a parameter, and finally displays the body of
the response.
"""
if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    try:
        query = sys.argv[1]
    except IndexError:
        query = ""
    q = {'q': query}
    r = requests.post(url, data=q)
    try:
        res = r.json()
    except ValueError:
        print("Not a valid JSON")
        exit()
    try:
        print("[{}] {}".format(res['id'], res['name']))
    except:
        print("No result")

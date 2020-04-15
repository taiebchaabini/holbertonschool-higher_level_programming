#!/usr/bin/python3
import requests
import sys
"""
Python script that takes in a URL and an email address, sends a POST request to
the passed URL with the email as a parameter, and finally displays the body of
the response.
"""
if __name__ == "__main__":
    url = sys.argv[1]
    try:
        r = requests.get(url)
        print(r.text)
    except:
        print(r.status_code)

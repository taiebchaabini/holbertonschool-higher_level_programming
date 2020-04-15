#!/usr/bin/python3
import requests
import sys
"""
Python script that takes in a URL and an email address, sends a POST request to
the passed URL with the email as a parameter, and finally displays the body of
the response.
"""
if __name__ == "__main__":
    try:
        url = sys.argv[1]
        r = requests.get(url)
        status_code = r.status_code
        raisecheck = r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError:
        print('Error code:', status_code)

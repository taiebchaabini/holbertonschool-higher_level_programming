#!/usr/bin/python3
import urllib.request
"""
Python script that fetches https://intranet.hbtn.io/status
"""
if __name__ == "__main__":
    url = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode('ascii'))

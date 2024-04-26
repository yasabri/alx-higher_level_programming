#!/usr/bin/python3
""" script that
 take in a URL
 sends request to URL and displays value
 X-Request-Id variable found in header ofthe response
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))

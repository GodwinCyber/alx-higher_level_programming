#!/usr/bin/python3
"""Python script that takes in a URL and an email,
   sends a POST request to the passed URL with
   the email as a parameter, and displays the body
   of the response (decoded in utf-8)
"""
import urllib.request
import sys
import urllib.parse
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    request = urllib.request.Request(url, data.encode('ascii'))
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error: {}".format(e.reason))

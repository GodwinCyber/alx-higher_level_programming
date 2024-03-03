#!/usr/bin/python3
"""take in URL, send request to the URL and display the value of the
    X-Request-Id variable foundin the header"""

import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Requrst-Id')
        print(x_request_id)

#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
   and uses the GitHub API to display your id
   to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get("http://api-github.com/user",
                            auth=(username, password))
    user = response.json()
    print(user.get("id"))

#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
   to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post("http://0.0.0.0:80/search_user",
                             data={"q": letter})
    try:
        user = response.json()
        if user == {}:
            print("[{}] {}".format(user.get("id"), user.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
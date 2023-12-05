#!/usr/bin/python3
"""define the function that read files"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")

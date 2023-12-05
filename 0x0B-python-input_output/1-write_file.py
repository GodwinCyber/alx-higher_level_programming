#!/usr/bin/python3
"""define the function that write string to files"""


def write_file(filename="", text=""):
    """write string to a file and return the text"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)

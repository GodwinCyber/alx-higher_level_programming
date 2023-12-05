#!/usr/bin/python3
"""define the function that append string at end of file"""


def append_write(filename="", text=""):
    """append the string at end of the text and return
    the number of charater added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)

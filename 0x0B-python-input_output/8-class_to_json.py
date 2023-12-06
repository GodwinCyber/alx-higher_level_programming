#!/usr/bin/python3
"""Define a python class-to-json"""


def class_to_json(obj):
    """returns the dictionary description
    with simple data structure
    """
    return obj.__dict__

#!/usr/bin/python3
"""Define Class to JSON"""
import json



def class_to_json(obj):
    """returns the dictionary description
    with simple data structure
    """
    return obj.__dict__

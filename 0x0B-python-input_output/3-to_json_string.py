#!/usr/bin/python3
"""define the function of JSON representation"""
import json


def to_json_string(my_obj):
    """return the JSON representation of an object"""
    return json.dumps(my_obj)

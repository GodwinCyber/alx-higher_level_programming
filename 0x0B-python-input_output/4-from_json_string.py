#!/usr/bin/python3
"""define the function of JSON representating data structure"""
import json


def from_json_string(my_str):
    """return an object data structure representation"""
    return json.loads(my_str)

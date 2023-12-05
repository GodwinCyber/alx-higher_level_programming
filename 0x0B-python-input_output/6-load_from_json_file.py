#!/usr/bin/python3
"""define the function of JSON representating data structure"""
import json


def load_from_json_file(filename):
    """writes an Object to a text file, using a JSON representation:"""
    with open(filename) as f:
        return json.load(f)

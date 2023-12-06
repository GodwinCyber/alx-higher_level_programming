#!/usr/bin/python3
"""Adds all arguments to a Python list"""
import json
import sys

def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation:"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return json.dump(my_obj, f)


def load_from_json_file(filename):
    """writes an Object to a text file, using a JSON representation:"""
    with open(filename) as f:
        return json.load(f)

my_list = []
json_file = "add_item.json"

try:
    my_new_list = load_from_json_file(json_file)
except FileNotFoundError:
    my_new_list = []

for arg in range(1, len(sys.argv)):
    my_list.append(sys.argv[arg])

my_new_list.extend(my_list)

save_to_json_file(my_new_list, json_file)

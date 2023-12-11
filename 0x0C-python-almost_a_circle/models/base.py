#!/usr/bin/python3
"""Define a base class that manage id without duplicate"""
import json


class Base:
    """Represent the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initiate the class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

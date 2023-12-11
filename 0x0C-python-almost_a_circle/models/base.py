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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filname = cls.__name__ + ".json"
        if list_objs is not None:
            dictionary_list = [obj.to_dictionary() for obj in list_objs]
        else:
            dictionary_list = []

        json_string = cls.to_json_string(dictionary_list)
        try:
            with open(filname, "w") as jsonfile:
                jsonfile.write(json_string)
        except IOError:
            print("Error: cannot write to file")

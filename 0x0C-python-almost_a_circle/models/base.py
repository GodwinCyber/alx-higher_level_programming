#!/usr/bin/python3
"""Define a base class that manage id without duplicate"""
import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy = cls(1)
            else:
                dummy = cls()
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a file"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        else:
            result = []
            with open(filename, "r") as jsonfile:
                dictionary_list = json.load(jsonfile)
                for dictionary in dictionary_list:
                    instance = cls.create(**dictionary)
                    result.append(instance)
                    return result

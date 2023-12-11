#!/usr/bin/python3
"""Define a base class that manage id without duplicate"""

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

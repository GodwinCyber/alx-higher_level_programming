#!/usr/bin/python3
"""LockedClass module"""


class LockedClass:
    """class that allow atribute to call only first_name"""
    __slots__ = ("first_name",)

    def __init__(self, first_name=""):
        """initializing the first_name attribute"""
        self.first_name = first_name

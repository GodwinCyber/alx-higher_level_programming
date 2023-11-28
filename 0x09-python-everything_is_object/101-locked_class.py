#!/usr/bin/python3
"""LockedClass module"""


class LockedClass:
    __slots__ = ("first_name",)
    """class that allow atribute call first_name"""

    def __init__(self, first_name=""):
        """initializing the first_name attribute"""
        self.first_name = first_name

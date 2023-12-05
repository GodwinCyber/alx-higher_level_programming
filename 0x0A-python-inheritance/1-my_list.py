#!/usr/bin/python3
"""define class that inherits from the list"""


class MyList(list):
    """ class MyList that inherits from list"""
    def print_sorted(self):
        """print the list but sorted ascending sort"""
        print(sorted(self))

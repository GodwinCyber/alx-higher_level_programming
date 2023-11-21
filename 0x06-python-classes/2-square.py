#!/usr/bin/python3
"""defines a clas Square"""


class Square:
    """defines a square by it's size"""

    def __init__(self, size=0):
        """initialize a square by Private instance attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

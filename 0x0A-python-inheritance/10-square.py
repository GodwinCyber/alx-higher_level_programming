#!/usr/bin/python3
"""class"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ class Square that inherits from Rectangle"""

    def __init__(self, size):
        """initialization"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

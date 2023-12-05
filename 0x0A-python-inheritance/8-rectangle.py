#!/usr/bin/python3
"""rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheruted from BaseGeometry"""

    def __init__(self, width, height):
        """initailization"""
        super().integer_validator("height", width)
        super().integer_validator("width", height)
        self.__height = height
        self.__width = width

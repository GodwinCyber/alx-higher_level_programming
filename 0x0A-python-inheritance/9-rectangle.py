#!/usr/bin/python3
"""define rectangle SubClass"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheruted from BaseGeometry"""
    def __init__(self, width, height):
        """initailization"""
        super().integer_validator("height", width)
        super().integer_validator("width", height)
        self.__height = height
        self.__width = width

    def area(self):
        """impleted the area"""
        return self.__height * self.__width

    def __str__(self):
        """return the rectangle description"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

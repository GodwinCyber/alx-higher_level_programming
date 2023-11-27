#!/usr/bin/python3
"""defines a class Rectangle"""


class Rectangle:
    """defines a rectangle by its width and height"""

    def __init__(self, width=0, height=0):
        """initializes a rectangle with a private instance
        attribute width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """return the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

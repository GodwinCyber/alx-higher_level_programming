#!/usr/bin/python3
"""Define Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represengt rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialise the class instructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """set the rectangle width"""
            return self.__width

        @width.setter
        def self(self, value):
            """the width setter"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """set th height of rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            """rectangle height setter"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """set the x cordinate of rectangel"""
            return self.__x

        @x.setter
        def x(self, value):
            """rectangle cordinate x setter"""
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """set the y cordinate of the rectangle"""
            return self.__y

        @y.setter
        def y(self, value):
            """rectangle cordinate y setter"""
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

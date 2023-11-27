#!/usr/bin/python3
"""defines a class Rectangle"""


class Rectangle:
    """defines a rectangle by its width and height"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes a rectangle with a private
        instance attribute width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """return the string that represent rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        s = ""

        for i in range(self.__height):
            s += str(self.print_symbol) * self.__width

            if i < self.__height - 1:
                s += "\n"
        return s

    def __repr__(self):
        """return the string that represent a rectangle
        that can be evaluated by eval
        """
        return ("Rectangle {}, {}".format(self.__width, self.__height))

    def __del__(self):
        """print a message when instance of rectangle is deleted"""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """retun new Rectangle instanc with width == height == size"""
        return cls(size, size)

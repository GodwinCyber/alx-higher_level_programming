#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """defines a square by its size"""

    def __init__(self, size=0):
        """initializes a square with a private instance attribute size"""
        self.size = size

    @property
    def size(self):
        """returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def __eq__(self, other):
        """compares two squares by their area for equality"""
        if isinstance(other, Square):
            return self.area() == other.area()

    def __ne__(self, other):
        """compares two squares by their area for inequality"""
        if isinstance(other, Square):
            return self.area() != other.area()

    def __lt__(self, other):
        """compares two squares by their area for less than"""
        if isinstance(other, Square):
            return self.area() < other.area()

    def __le__(self, other):
        """compares two squares by their area for less than or equal to"""
        if isinstance(other, Square):
            return self.area() <= other.area()

    def __gt__(self, other):
        """compares two squares by their area for greater than"""
        if isinstance(other, Square):
            return self.area() > other.area()
     
    def __ge__(self, other):
        """compares two squares by their area for greater than or equal to"""
        if isinstance(other, Square):
            return self.area() >= other.area()

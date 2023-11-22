#!/usr/bin/python3
"""defines a clas Square"""


class Square:
    """defines a square by it's size"""

    def __init__(self, size=0):
        """initialize a square by Private instance attribute"""
        self.size = size

    @property
    def size(self):
        """return the size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the siz of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """print square with charcter #"""
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print()
        if self.__size == 0:
            print()

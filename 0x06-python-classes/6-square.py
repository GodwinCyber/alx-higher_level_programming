#!/usr/bin/python3
"""defines a clas Square"""


class Square:
    """defines a square by it's size"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize a square by Private instance attribute"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """retrieve position and make it private"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position private"""
        if not isinstance(value, tuple) or len(value) != 2 or not all(
                isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """print square with charcter #"""
        if self.__size == 0:
            print()
            return
        [print() for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print()

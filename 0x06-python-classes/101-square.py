#!/usr/bin/python3

class Square:
    """defines a square by its size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes a square with a private instance attribute size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2 or not all(
            isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """returns a string representation of the square"""
        s = ""
        if self.__size == 0:
            return s
        else:
            for i in range(self.__position[1]):
                s += "\n"
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    s += " "
                for j in range(self.__size):
                    s += "#"
                if i < self.__size - 1:
                    s += "\n"
        return s

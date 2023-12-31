#!/usr/bin/python3
"""Define Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represents rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")  # Change made here
        if value <= 0:
            raise ValueError("width must be > 0")  # Change made here
        self.__width = value

    @property
    def height(self):
        """Get the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")  # Change made here
        if value <= 0:
            raise ValueError("height must be > 0")  # Change made here
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the rectangle x coordinate"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")  # Change made here
        if value < 0:
            raise ValueError("x must be >= 0")  # Change made here
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the rectangle y coordinate"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")  # Change made here
        if value < 0:
            raise ValueError("y must be >= 0")  # Change made here
        self.__y = value

    def area(self):
        """return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """print the rectangle with character #"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """return the string that represent rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """adding attribute to each other"""
        attributes = ["id", "width", "height", "y", "x"]
        for i, arg in enumerate(args):
            setattr(self, attributes[i], arg)
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

#!/usr/bin/python3
"""Define class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represnt class square inherited by rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initailise the class constructor"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """setting the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

#!/usr/bin/python3


class MyInt(int):
    """MyInt is a rebel. MyInt has == and
!= operators inverted
"""
    def __init__(self, value):
        """initialise value of MyInt"""
        self.value = value

    def __eq__(self, other):
        """Override the == operator to return
        the opposite of the default
        """
        return self.value != other

    def __ne__(self, other):
        """Override the != operator to return
        the opposite of defualt"""
        return self.value == other

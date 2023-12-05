#!/usr/bin/python3
"""define class of obj"""


def inherits_from(obj, a_class):
    """return true if the obj is insatnce
    that is inherited
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

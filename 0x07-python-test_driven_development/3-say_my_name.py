#!/usr/bin/python3
"""My name is <first name> <last name>"""
    
def say_my_name(first_name, last_name=""):
    """return the value of my full name
    Both first name and last name must be a string otherwise
    raise:
        TypeError it must a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("my name is {} {}".format(first_name, last_name))

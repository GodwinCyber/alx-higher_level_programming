#!/usr/bin/python3
"""define an integer addition function"""

def add_integer(a, b=98):
    """add two integer or float and return integer
    Argument are typecasted before addition is performed

    Raises:
       TyperError is raised if either a or b is not int of float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

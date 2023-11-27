#!/usr/bin/python3
"""prints a square with the character #."""

def print_square(size):
    """size of the lenght of square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size mut be an integer")
    
    for i in range(size):
        print("#" * size)

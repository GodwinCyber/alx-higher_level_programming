#!/usr/bin/python3

def uppercase(str):
    """print string in upper case."""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - 32)
        print("{}".format(c), end='')
    print("")

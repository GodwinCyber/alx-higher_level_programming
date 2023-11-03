#!/usr/bin/python3

def magic_calculation(a, b):
    add = None
    sub = None

    if a < b:
        add, sub = __import__('magic_calculation_102', globals(), locals(), ('add', 'sub'), 0)
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
    else:
        sub = __import__('magic_calculation_102', globals(), locals(), ('add', 'sub'), 0)
        c = sub(a, b)

    return c

#!/usr/bin/python3

for i in range(0, 26):
    c = chr(ord('z') - i)
    if i % 2 == 1:
        c = chr(ord(c) - ord('a') + ord('A'))
    print("{}".format(c), end='')

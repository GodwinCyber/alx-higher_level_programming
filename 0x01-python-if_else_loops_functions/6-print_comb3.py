#!/usr/bin/python3

count = 0

for i in range(9):
    count += 1
    for j in range(i * 10 + count, i * 10 + 10):
        if j == 89:
            print(89)
        else:
            print("{:02d}, ".format(j), end='')

#!/usr/bin/python3

import sys

    total_count = len(sys.argv) - 1

    if total_count == 0:
        print("0 arguments.")
    elif total_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(total_count))

    for i in range(total_count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

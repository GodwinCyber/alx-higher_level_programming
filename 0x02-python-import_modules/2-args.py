#!/usr/bin/python3

import sys

def print_arguments():
    num_arguments = len(sys.argv) -1
    print("{} argument".format(num_arguments,
        "s" if num_arguments != 1 else "", ":"
        if num_arguments > 0 else "."))

    for i in range(1, len(sys.argv)):
        argument = sys.argv[i]
        print("{}: {}".format(i, argument))

if __name__ == "__main__":
    print_arguments()

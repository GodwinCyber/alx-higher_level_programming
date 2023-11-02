#!/usr/bin/python3

import sys

def print_arguments():
    num_argument = len(sys.argv) -1
    print("{} arguments".format(num_argument))

    for i in range(1, len(sys.argv)):
        argument = sys.argv[i]
        print("{}: {}".format(i, argument))

if __name__ == "__main__":
    print_arguments()

#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    size = len(list_of_integers)
    mid_size = size
    mid = size // 2

    if size == 0:
        return None

    if size == 1:
        return list_of_integers[0]

    while True:
        mid_size = mid_size // 2
        if (mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if mid_size // 2 == 0:
                mid_size = 2
            mid = mid + mid_size // 2
        elif mid_size > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if mid_size // 2 == 0:
                mid_size = 2
            mid = mid - mid_size // 2
        else:
            return list_of_integers[mid]

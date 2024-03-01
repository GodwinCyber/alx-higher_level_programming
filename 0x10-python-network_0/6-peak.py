#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    # mid is the size of the current search range
    # mid is the middle index of the current search range
    size = len(list_of_integers)
    mid_size = size
    mid = size // 2
    # Check if list is empty
    if size == 0:
        return None
    # Check if list has only one element
    if size == 1:
        return list_of_integers[0]
    # Update the size of the search range by half
    # If right neighbor is greater, search in right half
    # If the search range is too small, increase it by 1
    # Update the middle index by moving to the right
    # If left neighbor is greater, search in left half
    # If the search range is too small, increase it by 1
    # Update the middle index by moving to the left
    # If neither neighbor is greater, mid is a peak
    # Return the peak element

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

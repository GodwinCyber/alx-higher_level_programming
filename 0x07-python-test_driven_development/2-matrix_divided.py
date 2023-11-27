#!/usr/bin/python3
"""define all element of the matrix"""

def matrix_divided(matrix, div):
    """all element in the list of the lsit must be int, float
    raise:
          TyepeError matrix mmust be a matrix...
    Each matrix must be equal size.
    raise
          TypeError all matrix must be the same size
    div is not divisible by o
    raise
          ZeroDivisionError not divisible by 0
    """
    if not isinstance (matrix, list) or not all(isinstance (row, list) and all(isinstance (x, 
    (int, float)) for x in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if ((not isinstance(div, int) and not isinstance(div, float))):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        
        for x in row:
            new_x = round(x / div, 2)
            new_row.append(new_x)
        new_matrix.append(new_row)
    return new_matrix

#!/usr/bin/python3
"""Division of matrix"""


def matrix_divided(matrix, div):

    """Validate matrix"""
    if not all(isinstance(row, list) for row in matrix) \
        or not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    size = len(matrix[0])
    if not all(len(row) == size for  row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div,(int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix

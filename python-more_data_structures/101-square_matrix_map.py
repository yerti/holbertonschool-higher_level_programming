#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    result = ([list(map(lambda x: x * x, i)) for i in matrix])
    return result

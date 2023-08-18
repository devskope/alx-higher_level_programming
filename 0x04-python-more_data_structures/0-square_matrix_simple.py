#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Compute square of all integers in 2d matrix."""
    return [list(map(lambda x: x ** 2, row)) for row in matrix]

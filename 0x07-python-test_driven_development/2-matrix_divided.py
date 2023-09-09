#!/usr/bin/python3
"""Define matrix division function."""


def matrix_divided(matrix, div):
    """Perform division on all elements of a matrix.

    Args:
        matrix (list): List of lists (ints or floats).
        div (int/float): The divisor.
    Raises:
        TypeError: If matrix contains non-numbers.
        TypeError: If matrix contains rows of different sizes.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.
    Returns:
        new matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("Matrix must be of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be numeric")

    if div == 0:
        raise ZeroDivisionError("Division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])

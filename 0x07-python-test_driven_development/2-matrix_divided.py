#!/usr/bin/python3
"""Module that defines matrix divisio"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix(list): A list of lists containing int or float
        div (int/float): divisor
    Raises:
        TypeError: If matrix contains non-numbers
        TypeError: If matrix contains row of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: if divisor is zero
    Returns: New matrix with results of division
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all (isinstance(row, list) for row in matrix) or
            not all ((isinstance(elem, int) or isinstance(elem, float))
                for elem in [num for row in matrix for num in row])):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all (len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, float) and not isinstance(div, int):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x /div, 2), row)) for row in matrix])
    





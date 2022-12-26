#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ Compute squares of elements in a matrix"""
    if not matrix:
        return None
    new_matrix = []
    for i in matrix:
        new = list(map((lambda x: x*x), i))
        new_matrix.append(new)
    return (new_matrix)

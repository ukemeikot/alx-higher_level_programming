#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix == []:
        return []
    new_matrix = []
    for row in matrix:
        new_matrix.append([item**2 for item in row])
    return new_matrix

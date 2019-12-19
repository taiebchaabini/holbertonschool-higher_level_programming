#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([row[i] for row in matrix])
    for i in range(len(matrix)):
        for b in range(len(matrix[i])):
            new_matrix[i][b] = matrix[i][b] * matrix[i][b]
    return new_matrix

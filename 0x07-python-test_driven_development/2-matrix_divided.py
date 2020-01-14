#!/usr/bin/python3
def matrix_divided(matrix, div):
    types = (int, float)
    errorMsg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(errorMsg)
    if len(matrix) == 1:
        if len(matrix[0]) == 1 and isinstance(matrix[0][0], types) is True:
            return [[matrix[0][0]/3]]
            
    if len(matrix) <= 1:
        raise TypeError(errorMsg)
    for i in matrix:
        if type(i) is not list or len(i) is 0:
            raise TypeError(errorMsg)
    if (isinstance(div, types) is False):
        raise TypeError("div must be a number")
    c = list(map(lambda x:
             list(map(lambda i: isinstance(i, types), x)), matrix))
    if len(matrix) is 0:
        raise TypeError(errorMsg)
    for i in c:
        if False in i:
            raise TypeError(errorMsg)
    matrixlen = list(map(lambda x: len(x), matrix))
    if (len(set(matrixlen)) != 1):
        raise TypeError("Each row of the matrix must have the same size")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda x: list(map(lambda i:
                      round(i / div, 2), x)), matrix))
    return (new_matrix)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")

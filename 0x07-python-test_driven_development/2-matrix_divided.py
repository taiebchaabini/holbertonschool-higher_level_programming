#!/usr/bin/python3
def matrix_divided(matrix, div):
    types = (int, float)
    if (isinstance(div, types) is False):
        raise TypeError("div must be a number")
    c = list(map(lambda x:
             list(map(lambda i: isinstance(i, types), x)), matrix))
    errorMsg = "matrix must be a matrix (list of lists) of integers/floats"
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
    doctest.testfile("2-matrix_divided.txt")

#!/usr/bin/python3
def matrix_divided(matrix, div):
    '''divides a matrix by @div'''

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    for row in matrix:
        if len(row) == len(matrix[0]):
            for el in row:
                if type(el) != int and type(el) != float:
                    raise TypeError("matrix must be a matrix \
                                    (list of lists) of integers/floats")
        else:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []

    for row in matrix:
        n_list = []  # Create a new list for each row
        for el in row:
            n_list.append(round(el / div, 2))
        new_matrix.append(n_list)

    return new_matrix

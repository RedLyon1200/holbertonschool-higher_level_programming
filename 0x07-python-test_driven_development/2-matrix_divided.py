#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix.

    Args:
        matrix: A list of integers of floats.
        div: divisor
    Raises:
        TypeError:
            if the matrix is not a list of lists of integers or floats
            if the rows of the matrix are not of the same size
            id div is not a integer or float
        ZeroDivisionError:
            if div is zero
    Return:
        A new matrix with the results"""

    lenght = []
    invalid_mtx = 'matrix must be a matrix (list of lists) of integers/floats'
    invalid_div = 'div must be a number'

    if div is True or div is False:
        raise TypeError(invalid_div)

    if type(div) not in [int, float]:
        raise TypeError(invalid_div)

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(invalid_mtx)

    for listt in matrix:
        if type(listt) is not list or len(listt) == 0:
            raise TypeError(invalid_mtx)

        lenght.append(len(listt))

        for num in listt:
            if type(num) not in [int, float]:
                raise TypeError(invalid_mtx)

    for size in lenght:
        if size != lenght[0]:
            raise TypeError('Each row of the matrix must have the same size')

    return [[round(num / div, 2) for num in listt] for listt in matrix]

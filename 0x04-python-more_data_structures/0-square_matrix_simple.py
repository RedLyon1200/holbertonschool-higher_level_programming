#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq = []

    for elm in matrix[:]:
        sq.append(list(map(lambda x: x ** 2, elm)))

    return sq

#!/usr/bin/python3
""" list of lists of integers representing the Pascal’s triangle """


def pascal_triangle(n):
    """
    Args:
        n ([int]): [n times]

    Returns:
        [type]: [a list of lists of integers representing
        the Pascal’s triangle of n:]
    """
    li = [[1]]
    if n <= 0:
        return []
    for row in range(1, n):
        li.append([1])
        for count in range(row):
            try:
                num = li[row - 1][count + 1] + li[row - 1][count]
            except Exception:
                num = 1
            if row - 1 == count:
                num = 1
            li[row].append(num)
    return li

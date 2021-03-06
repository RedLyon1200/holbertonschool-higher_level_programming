#!/usr/bin/python3
def print_square(size):
    """[unction that prints a square with the character #]

    Arguments:
        size {[int]} -- [the size length of the square]

    Raises:
        TypeError: [size must be an integer]
        ValueError: [size must be >= 0]
    """

    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for pos in range(size):
        print('#' * size)

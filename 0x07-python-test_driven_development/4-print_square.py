#!/usr/bin/python3
def print_square(size):
    """
    function that prints a square with the character #


    Args:
        size: the size length of the square
    Raises:
        TypeError:
            size must be an integer
        ValueError:
            size must be >= 0
    """
    if type(size) not in [int, float]:
        raise TypeError('size must be an integer')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for pos in range(int(size)):
        print('#' * int(size))

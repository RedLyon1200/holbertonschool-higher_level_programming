#!/usr/bin/python3
"""define class Square"""


class Square:
    """init to define size"""
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError('size must be >= 0')
            self.__size = size
        except TypeError:
            raise TypeError('size must be an integer')

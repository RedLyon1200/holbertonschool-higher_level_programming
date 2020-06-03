#!/usr/bin/python3
"""[function that counts the line number of a file]
    """


def number_of_lines(filename=""):
    """
    Keyword Arguments:
        filename {str} -- [file path] (default: {""})

    Returns:
        [int] -- [the number of lines of a text file]
    """
    with open(filename, encoding='UTF-8') as f_obj:
        return (len(f_obj.readlines()))

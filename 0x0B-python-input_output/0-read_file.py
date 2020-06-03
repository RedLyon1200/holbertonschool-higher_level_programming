#!/usr/bin/python3
"""[function that reads a text file (UTF8) and prints it to stdout:]
    """


def read_file(filename=""):
    """
    Keyword Arguments:
        filename {str} -- [file path] (default: {""})
    """
    with open(filename, encoding='UTF-8') as f_obj:
        contents = f_obj.read()
        print(contents, end='')

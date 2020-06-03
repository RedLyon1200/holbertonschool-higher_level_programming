#!/usr/bin/python3
"""[function that reads n lines of a text file (UTF8) and prints it to stdout:]
    """


def read_lines(filename="", nb_lines=0):
    """
    Keyword Arguments:
        filename {str} -- [file path] (default: {""})
        nb_lines {int} -- [number of lines to read] (default: {0 - all})
    """
    with open(filename, encoding='UTF-8') as f_obj:
        if nb_lines <= 0:
            print(f_obj.read(), end='')
        else:
            contents = f_obj.readlines()
            print(''.join(contents[:nb_lines]), end='')

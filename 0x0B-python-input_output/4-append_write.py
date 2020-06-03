#!/usr/bin/python3
"""[function that appends a string at the end of a text file]
    """


def append_write(filename="", text=""):
    """
    Keyword Arguments:
        filename {str} -- [file path] (default: {""})
        text {str} -- [text to add to the file] (default: {""})

    Returns:
        [int] -- [the number of characters written]
    """
    with open(filename, 'a', encoding='UTF-8') as f_obj:
        f_obj.write(text)
    return len(text)

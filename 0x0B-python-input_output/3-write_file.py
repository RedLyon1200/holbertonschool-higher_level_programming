#!/usr/bin/python3
"""[function that writes a string to a text file]
    """


def write_file(filename="", text=""):
    """
    Keyword Arguments:
        filename {str} -- [file path] (default: {""})
        text {str} -- [text to add to the file] (default: {""})

    Returns:
        [int] -- [the number of characters written]
    """
    with open(filename, 'w', encoding='UTF-8') as f_obj:
        f_obj.write(text)
    return len(text)

#!/usr/bin/python3
"""[function that inserts a line of text to a file,
    after each line containing a specific string]
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Args:
        filename (str, optional): [description]. Defaults to "".
        search_string (str, optional): [str to sears]. Defaults to "".
        new_string (str, optional): [str to add after search_str]
        . Defaults to "".
    """
    with open(filename, 'r+', encoding='UTF-8') as f_obj:
        my_list = []

        for line in f_obj:
            my_list.append(line)
            if line.count(search_string) > 0:
                my_list.append(new_string)
        content = ''.join(my_list)
        f_obj.seek(0)
        f_obj.write(content)

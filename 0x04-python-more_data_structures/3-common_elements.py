#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []

    for w in set_1:
        for x in set_2:
            if x == w:
                new_list.append(w)
    return new_list

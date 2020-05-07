#!/usr/bin/python3
def rec(new_list, set):
    for w in set:
        if w in new_list[:]:
            pos = 1

            while pos < len(new_list):
                if new_list[pos] == w:
                    del new_list[pos]
                pos += 1
            continue
        new_list.append(w)


def only_diff_elements(set_1, set_2):
    new_list = []

    rec(new_list, set_1)
    rec(new_list, set_2)

    return new_list

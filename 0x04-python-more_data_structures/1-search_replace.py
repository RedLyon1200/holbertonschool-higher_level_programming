#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    count = 1

    for w in my_list[:]:
        if w == search:
            new_list.append(replace)
        else:
            new_list.append(w)
    return new_list

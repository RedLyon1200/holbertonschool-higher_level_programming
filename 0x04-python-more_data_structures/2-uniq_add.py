#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    result = 0

    if my_list:
        for elm in my_list[:]:
            if elm in new_list[:]:
                continue
            new_list.append(elm)
            result += elm
    return result

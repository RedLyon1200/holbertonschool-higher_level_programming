#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = 0
        for x in my_list:
            if x > max:
                max = x
        return max
    return None

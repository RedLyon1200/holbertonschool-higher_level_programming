#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum = 0
        for elm in my_list:
            sum += int(elm)
        return sum / len(my_list)
    return 0

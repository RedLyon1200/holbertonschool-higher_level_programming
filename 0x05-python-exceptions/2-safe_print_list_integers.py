#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    integerscount = 0
    while count < x:
        try:
            print("{:d}".format(my_list[count]), end="")
            integerscount += 1
        except (ValueError, TypeError):
            print(end="")
        count += 1
    print()
    return integerscount

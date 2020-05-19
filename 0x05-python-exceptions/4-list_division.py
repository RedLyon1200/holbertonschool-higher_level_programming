#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    length = []
    count = 0
    while count < list_length:
        try:
            result = my_list_1[count] / my_list_2[count]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            length.append(result)
        count += 1
    return length

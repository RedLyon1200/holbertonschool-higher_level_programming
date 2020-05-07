#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    i = 0

    if roman_string.isalpha():
        while i < len(roman_string):
            x = roman_string[i]
            if x == 'I':
                result += 1
            elif x == 'V':
                result += 5
            elif x == 'X':
                result += 10
            elif x == 'L':
                result += 50
            elif x == 'C':
                result += 100
            elif x == 'D':
                result += 500
            elif x == 'M':
                result += 1000
            else:
                return 0 
            i += 1
        return result
    return 0

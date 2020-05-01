#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    def errmsg():
        print("Unknown operator. Available operators: +, -, * and /")

    def ex(a, o, b):
        from calculator_1 import sub, add, mul, div
        if o == '+':
            print(a, o, b, '=', add(int(a), int(b)))
        elif o == '-':
            print(a, o, b, '=', sub(int(a), int(b)))
        elif o == '*':
            print(a, o, b, '=', mul(int(a), int(b)))
        else:
            print(a, o, b, '=', div(int(a), int(b)))
    a = argv[1]
    b = argv[3]
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    o = argv[2]
    if o != '*' and o != '+' and o != '-' and o != '/':
        errmsg()
    else:
        ex(a, o, b)

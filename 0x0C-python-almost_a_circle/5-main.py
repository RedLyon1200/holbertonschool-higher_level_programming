#!/usr/bin/python3
""" 5-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 2, 1)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)

    s1 = Square(4)
    print(s1)

    s2 = Square(5)
    print(s2)

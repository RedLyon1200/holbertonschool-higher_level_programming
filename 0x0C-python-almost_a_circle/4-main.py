#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 15)
    r1.display()

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()

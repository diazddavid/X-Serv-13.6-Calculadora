#!/usr/bin/python3

import sys

try:
    _, operator, num1, num2 = sys.argv
except ValueError:
    print("You need a Mathematical Operator and two Numbers.")
    sys.exit("Maybe you have used * improperly. To use mult, write '\*' ")

PLUS = "+"
MINUS = "-"
MULT = "*"
DIV = "/"

try:
    num1, num2 = float(num1), float(num2)
except ValueError:
    sys.exit("You need floats")

if operator == PLUS:
    print(num1 + num2)
elif operator == MINUS:
    print(num1 - num2)
elif operator == MULT:
    print(num1 * num2)
elif operator == DIV:
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        sys.exit("You can't do a zero division")

print("Any valid Mathematical operator")
sys.exit("The valid Mathematical Operators are + - / *")

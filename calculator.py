#https://github.com/amorales5/lab10-CS-AM.git
#Partner 1: Crystal Schmitt
#Partner 2: Alexsis Morales

import math

def square_root(a):
    if a<0:
        raise ValueError ("ValueError, cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a, b)


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("ZeroDivisionError: Division by zero isn't allowed.") #raise ZeroDivisionError if a == 0
    return b / a

def log(a, b):
        if a <= 0 or a == 1:
            raise ValueError("ValueError: Base must be > 0 and not equal to 1")
        return math.log(b, a)

def exp(a, b):
    return a ** b

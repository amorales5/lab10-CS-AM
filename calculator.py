import math

def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    try:
        return b / a  #raise ZeroDivisionError if a == 0
    except ZeroDivisionError:
        print("Division by zero")
def log(a, b):
        if a <= 0 or a == 1:
            raise ValueError("ValueError: Base must be > 0 and not equal to 1")
        return math.log(a, b)
def exp(a, b):
    return a ** b



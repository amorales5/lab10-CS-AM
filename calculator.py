import math

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



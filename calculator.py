"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    try:
        return b / a   #raise ZeroDivisionError if a == 0
    except ZeroDivisionError:
        print("You can't divide by zero")
def log(a, b):
    try:
        return math.log(a,b)  #use math library + raise ValueError
    except ValueError:
        print("ValueError")
def exp(a,b):
    return a ** b

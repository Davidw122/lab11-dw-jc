"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.

Function	Required behavior
add(a,b)	a + b
subtract(a,b)	a - b
multiply(a,b)	a * b
divide(a,b)	b / a; raise ZeroDivisionError if a == 0
logarithm(a,b)	\(\log_a(b)\); validate base and argument
exponent(a,b)	a ** b


"""
import math
# First example
def add(a, b): 
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def logarithm(a, b):
    return math.log(a, b)
def exponent(a, b):
    return a ** b



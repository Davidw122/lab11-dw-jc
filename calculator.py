# https://github.com/Davidw122/lab11-dw-jc
# Partner 1: David Weisglass
# Partner 2: Javier Castro



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

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

# Partner 1 work
def add(a, b):
    # Partner 1 version
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
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm base or argument")
    return math.log(b, a)
def exponent(a, b):
    return a ** b

#Partner 2 work

def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def log(a, b):
    return logarithm(a, b)
def exp(a, b):
    return a ** b




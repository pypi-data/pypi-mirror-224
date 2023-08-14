import math
from random import randint
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b
def add_one(a):
    return a+1
def sub_one(a):
    return a-1
def sq(a):
    return a**a
def sqrt(a):
    return math.sqrt(a)
def ex(a, b):
    return a**b
def cbrt(a):
    return a ** (1. / 3)
def randum(a, b):
    return randint(a, b)
def sin(a):
    return math.sin(a)
def cos(a):
    return math.cos(a)
def tan(a):
    return math.tan(a)
def fib(a, memo = {}):
    if a in memo:
        return memo[a]
    if a == 1 or a == 2:
        return 1
    else:
        memo[a] = fib(a - 1, memo) + fib(a - 2, memo)
        return memo[a]
def asin(a):
    return math.asin(a)
def acos(a):
    return math.acos(a)
def atan(a):
    return math.atan(a)
def atan2(a, b):
    return math.atan2(a, b)
   
def cosec(a):
    return 1/math.sin(a)
   
def cot(a):
    return 1/math.tan(a)

def sec(a):
    return 1/math.cos(a)
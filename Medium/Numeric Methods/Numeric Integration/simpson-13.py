from math import *
def f(x):
    return exp(x**2)

def simpson13(a,b,f):
    I=(b-a)*(f(a)+4*f((a+b)/2)+f(b))/6
    return I

a=0
b=1
print(simpson13(a,b,f))
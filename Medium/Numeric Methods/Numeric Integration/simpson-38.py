from math import *
def f(x):
    return exp(x**2)

def simpson38(a,b,f):
    h=(b-a)/3
    x1=a
    x2=a+h
    x3=x2+h
    x4=b
    I=(3/8)*(h)*(f(x1)+3*f(x2)+3*f(x3)+f(x4))
    return I

a=0
b=1
print(simpson38(a,b,f))
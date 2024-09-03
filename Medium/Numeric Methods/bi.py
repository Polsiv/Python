from math import *

tolerancia = 10*(-6)
a=0
b=2
Mold = 0
def f(x):
    return (exp(-x) -x)

flag = True

while flag:


    Mnew = (a+b)/2
    fa=f(a)
    fb=f(b)
    fm=f(Mnew)

    if fa * fm < 0:
       b=Mnew

    else:
       a = Mnew

    error = abs(a - b)
    if error < tolerancia:
        print(Mnew)
        flag = False

    else:
       Mold = Mnew
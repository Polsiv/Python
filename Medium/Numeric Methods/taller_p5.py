from math import exp

tol = 10**(-4)

def f(x):
    return (x**2 -12) 


def falsa_posicion(a, b):
    if f(a) * f(b) >= 0:
        return None

    c = a 

    while (b - a) >= tol:

        c = (a * f(b) - b * f(a) ) / (f(b) - f(a))

        if abs( f(c))  < tol:
            break

        if f(c) * f(a) < 0:
            b = c

        else :
            a = c

    return c

print(falsa_posicion(0,10))
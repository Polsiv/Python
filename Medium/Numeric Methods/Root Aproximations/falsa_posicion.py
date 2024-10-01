from math import exp

tol = 10**(-6)

def f(x):
    return (exp(-x) - x) 


def falsa_posicion(a, b):
    if f(a) * f(b) >= 0:
        return None

    c = a 

    while (b - a) >= tol:

        c = (a * f(b) - b * f(a) ) / (f(b) - f(a))

        if abs(c - b)  < tol:
            break

        if f(c) * f(a) < 0:
            b = c

        else :
            a = c

    return c

print(falsa_posicion(0, 2))
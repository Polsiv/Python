from math import exp

def f(x):
    return (exp(-x) - x) 

def f_prime(x, h):
    return (f( x + h) - f(x)) / h

def second_dev(x, h):
    return (1 / h**2) * (f(x + 2*h) - 2*f(x + h)  + f(x))


tol = 10**(-6)


def newton_rapshon(a):
    h = 10**(-4)
    flag = True
    a_old = a
    counter = 1
    while flag:

        a_new = a_old  - ((f(a_old) * f_prime(a_old, h)) / (f_prime(a_old, h)**2 - f(a_old) * second_dev(a_old, h) ))
        if abs((a_new - a_old) / a_new) < tol:
            flag = False

        a_old = a_new

        print(f'{counter}. {a_new}')
        counter += 1

newton_rapshon(3)
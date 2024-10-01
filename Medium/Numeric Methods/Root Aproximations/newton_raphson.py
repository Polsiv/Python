from math import exp

tol = 10**(-6)

def f(x):
    return x - 2

def f_prime(x):
    h = 10**(-6)
    return (f( x + h) - f(x)) / h

def newton_rapshon(a):
    flag = True
    a_old = a
    counter = 1
    while flag:

        a_new = a_old - f(a_old)/f_prime(a_old)
        if abs((a_new - a_old) / a_new) < tol:
            flag = False

        a_old = a_new

        print(f'{counter}. {a_new}')
        counter += 1

newton_rapshon(3)
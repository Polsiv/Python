from math import exp

tol = 10**(-6)

def f(x):
    return (exp(-x) - x) 

def f_secant(x, y):
    return (f(x) - f(y)) / (x - y)

def newton_rapshon(a, b):
    flag = True
    a_old = a
    counter = 1
    while flag:

        a_new = a_old - f(a_old)/f_secant(a,b)
        if abs((a_new - a_old) / a_new) < tol:
            flag = False
        
        
        a_old = a_new
        b = a_old

        print(f'{counter}. {a_new}')
        counter += 1

newton_rapshon(1, 2)
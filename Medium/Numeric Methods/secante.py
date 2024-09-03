from math import sqrt

tol = 10**(-6)

def f(x):
    n_i = 6.21
    
    return (1/2) * (x + sqrt(x**2 + 4*n_i**2)) - 16

def f_secant(x, y):
    return (f(x) - f(y)) / (x - y)

def secant(a, b):
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

secant(1, 2)
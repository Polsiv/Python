import numpy as np

def f(x):
    return x ** 2

def trapezoid(a, b, n):
    x = np.linspace(a, b, n + 1)
    dx = (b - a) / n  
    A = 0
    for i in range(1, len(x) - 1):
        A += 2 * f(x[i])
    
    I = dx * (f(x[0]) + A + f(x[-1])) / 2  
    return I

def romberg(a, b, n):
    matrix = np.zeros((n, n))

    for i in range(n):
        matrix[i, 0] = trapezoid(a, b, 2 ** i)

    for i in range(1, n):
        for j in range(i, n):
            matrix[j, i] = (4 ** i * matrix[j, i - 1] - matrix[j - 1, i -  1]) / (4 ** i - 1)

    return matrix

a = 0
b = 3
n = 3

print(romberg(a, b, n))

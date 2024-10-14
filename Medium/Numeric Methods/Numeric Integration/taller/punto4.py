import numpy as np
from math import sqrt

def f(x):
    return 3 ** x

def lagrange(a, b, n, f, x):

    sum = 0
    dx = np.linspace(a, b, n + 1)
    for i in range(n + 1):
        L = 1
        for j in range(n + 1):
            if i == j:
                continue
            
            else:
                L *= (x - dx[j]) / (dx[i] - dx [j])

        sum += L * f(dx[i])
    return sum


a = 0
b = 2 / 3
n = 3
x = 0.5
print(lagrange(a, b, n, f, x))
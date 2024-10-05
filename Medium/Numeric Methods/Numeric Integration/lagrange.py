import numpy as np

def f(x):
    return x**2

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


print(lagrange(0, 3, 4, f, 3))
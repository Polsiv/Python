
from numpy import linspace

def f(x):
    return x**2

def trapezoid(a, b, n):

    dx = (b-a)/n
    x_values = linspace(a, b, n + 1)
    sum = 0

    for i in range(1, n - 1):
        sum += f(x_values[i])
    
    sum *= 2
    
    area = (b-a) * ((f(a) + f(a + dx * n) + sum)/ (2 * n))

    return area

a = 0
b = 3
n = 10

print(trapezoid(a, b, n))
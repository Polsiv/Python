from numpy import linspace

def f(x):
    return x**2

def rieman(a, b, n):

    dx = (b - a)/n
    x_values = linspace(a, b, n + 1)
    total_area_left, total_area_right = 0, 0

    for i in range(0, n):

        total_area_left += dx * f(x_values[i])
        total_area_right += dx * f(x_values[i + 1])

    mean = (total_area_right + total_area_left)/ 2
    return mean

a = 0
b = 3
n = 10000

print(rieman(a, b, n))
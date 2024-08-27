from math import sin, sqrt

x_old = 3

def g(x):
    return 2*sin(sqrt(x)) - sqrt(x) + x

tol = 10**(-6)

for i in range(50):
    x_new = g(x_old)

    err = abs(x_new - x_old)
    if err < tol:
        break
    else:
        x_old = x_new

print(x_old)

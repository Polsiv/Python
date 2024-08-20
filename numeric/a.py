import math

x_old = 1

def g(x):
    return math.exp(-x)

tol = 10**(-6)

for i in range(50):
    x_new = g(x_old)

    err = abs(x_new - x_old)
    if err < tol:
        break
    else:
        x_old = x_new

print(x_old)

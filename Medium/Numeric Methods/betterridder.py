from math import sqrt, sin

def f(x):
    return 2 * sin(sqrt(x)) - sqrt(x)

def ridder(a, b):
    tol = 10**(-4)
    counter = 1
    flag = True

    if abs(f(a)) < tol:
        return a
    if abs(f(b)) < tol:
        return b

    while flag:
        if abs(a - b) / 2 < tol:
            flag = False
        else:
            m = (a + b) / 2
            x_3 = m + (b - m) * (f(m) / f(a)) / sqrt((f(m) / f(a))**2 - f(b) / f(a))

            if f(a) * f(x_3) < 0:
                b = x_3
            else:
                a = x_3

            print(f'{counter} : {x_3}')
            counter += 1

    return x_3

root = ridder(1, 5)
print(f'Root found: {root}')

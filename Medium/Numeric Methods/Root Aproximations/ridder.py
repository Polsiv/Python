from math import exp, sqrt, sin


def f(x):
    return 2*sin(sqrt(x)) - sqrt(x)


def ridder(a, b):
  
    tol = 10**(-4)
    counter = 1
    flag = True

    while flag:

        if abs((a - b) / 2) < tol:
            flag = False
        else:

            m = (a + b) / 2

            x_3 = m + (b - m) * (f(m) / f(a)) / sqrt( (f(m) / f(a))**2 - f(b) / f(a))

            if f(a) * f(b) < 0:
                b = a
                a = x_3
            else: 
                a = b
                b = x_3
        print(f'{counter} : {x_3}')
        
        counter += 1
    return x_3


ridder(1, 5)

        

        
        

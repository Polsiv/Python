
import numpy as np

def f(x):
    return x**2

def trapezoid(a, b, n):
    x = np.linspace(a, b, n + 1)
    dx=(b-a)
    A=0
    for i in range(1,len(x)-1):
        A+=(2*f(x[i]))
    
    I=dx*(f(x[0])+A+f(x[n]))/(2*n)
    return I



def romberg(a, b, n):
    
    col_act = 0
    matrix = np.zeros((n, n))

    for i in range(0, n):
        for j in range(0, n):

            if i == 0:
                matrix[j][i] = j
            
            elif i == 1:
                matrix[j][i] = trapezoid(a, b, 2 ** j)

            else:
                try:
                    matrix[j + 1][i] = (1 / (4 ** i - 1)) * (((4 ** i) * matrix[i][j - 1]) - matrix[i - 1][j - 1]) 
                except:
                    pass

    return matrix


a = 0
b = 3
n = 3

print(romberg(a, b, n))   
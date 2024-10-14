import numpy as np
from math import *


def f(x):
    match x:
        case 1:
            return 2
        case 2:
            return 3
        case 3:
            return 5
        case 4:
            return 4


def diferenciaDividida(x, fx):
    n = len(x)
    tabla = np.zeros((n, n))
    
    tabla[:, 0] = fx
    
    for j in range(1, n):
        for i in range(n - j):
            tabla[i, j] = (tabla[i + 1, j - 1] - tabla[i, j - 1]) / (x[i + j] - x[i])


    print(tabla)
    return tabla[0, :]

def polinomioNewton(coeficientes, puntos_x, valor):
    n = len(coeficientes)
    resultado = coeficientes[0]
    producto = 1.0  
    
    for i in range(1, n):
        producto *= (valor - puntos_x[i - 1])
        resultado += coeficientes[i] * producto
    
    return resultado

valor = 2.6
x = [1, 2, 3, 4]
fx = [f(i) for i in x]

coeficientes = diferenciaDividida(x, fx)


resultado = polinomioNewton(coeficientes, x, valor)
print(f"El valor interpolado en x = {valor} es: {resultado}")
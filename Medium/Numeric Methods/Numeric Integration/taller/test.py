import numpy as np
from math import *

def f(x):
    return x**2

def diferenciaDividida(x, fx):
    n = len(x)
    tabla = np.zeros((n, n))
    
    tabla[:, 0] = fx
    
    for j in range(1, n):
        for i in range(n - j):
            tabla[i, j] = (tabla[i + 1, j - 1] - tabla[i, j - 1]) / (x[i + j] - x[i])
    
    return tabla[0, :]

def polinomioNewton(x, coeficientes, puntos_x, valor):
    n = len(coeficientes)
    resultado = coeficientes[0]
    producto = 1.0  
    
    for i in range(1, n):
        producto *= (valor - puntos_x[i-1])
        resultado += coeficientes[i] * producto
    
    return resultado

a = 0
b = 3
n = 4

x = np.linspace(a, b, n)
fx = [f(i) for i in x]

coeficientes = diferenciaDividida(x, fx)

valor = 4
resultado = polinomioNewton(x, coeficientes, x, valor)

print(f"El valor interpolado en x = {valor} es: {resultado}")
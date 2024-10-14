import numpy as np
from math import *

# Función a interpolar
def f(x):
    return x**2

# Función para calcular las diferencias divididas
def diferenciaDividida(x, fx):
    n = len(x)
    # Crear una tabla de diferencias divididas con tamaño n x n
    tabla = np.zeros((n, n))
    
    # Primera columna de la tabla es simplemente f(x)
    tabla[:, 0] = fx
    
    # Llenar el resto de la tabla
    for j in range(1, n):
        for i in range(n - j):
            tabla[i, j] = (tabla[i + 1, j - 1] - tabla[i, j - 1]) / (x[i + j] - x[i])
    
    # Los coeficientes están en la primera fila
    return tabla[0, :]

# Función para evaluar el polinomio de Newton en un punto dado
def polinomioNewton(x, coeficientes, puntos_x, valor):
    n = len(coeficientes)
    # Inicializamos el polinomio con el primer coeficiente (el término independiente)
    resultado = coeficientes[0]
    producto = 1.0  # Variable para construir los productos (x - x_0)(x - x_1)...
    
    for i in range(1, n):
        producto *= (valor - puntos_x[i-1])
        resultado += coeficientes[i] * producto
    
    return resultado

# Parámetros
a = 0
b = 3
n = 4

# Generar los puntos x equidistantes y calcular f(x)
x = np.linspace(a, b, n)
fx = [f(i) for i in x]

# Calcular diferencias divididas
coeficientes = diferenciaDividida(x, fx)

# Elegir un valor para evaluar el polinomio interpolador
valor = 4
resultado = polinomioNewton(x, coeficientes, x, valor)

# Imprimir el resultado
print(f"El valor interpolado en x = {valor} es: {resultado}")
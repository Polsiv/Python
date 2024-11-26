import numpy as np
import matplotlib.pyplot as plt

x = np.array([150, 153, 156, 159, 162, 165, 168, 171, 174, 177, 180])  
y = np.array([75.0, 76.3, 78.2, 80.0, 80.1, 82.0, 84.4, 85.7, 86.8, 88.6, 89.7]) 
n = len(x)

sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x2 = np.sum(x**2)
sum_xy = np.sum(x * y)

# punto a:
a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a0 = (sum_y - a1 * sum_x) / n

def y_est(x):
    return a0 + a1*x

print("Recta de Estimación")
print(f'Yest = {a0} + {a1}x')  


# punto b:
plt.scatter(x, y, color="blue", label="Datos")
x_vals = np.linspace(min(x), max(x), 100)
y_vals = y_est(x_vals)
plt.plot(x_vals, y_vals, color="red", label="Recta de regresión")

plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")
plt.title("Gráfico de dispersión y recta de regresión")
plt.legend()
plt.grid()
plt.show()


# punto c:

y_mean = np.mean(y)

SST = np.sum((y - y_mean) ** 2)

y_est_vals = y_est(x)
SSR = np.sum((y_est_vals - y_mean) ** 2)

SSE = np.sum((y - y_est_vals) ** 2)

print(f'Variacion Total: {SST}')
print(f'Variacion Explicada: {SSR}')
print(f'Variacion Inexplicada: {SSE}')


# Punto d:
r=np.sqrt(SSR/SST)
print(f'Coeficiente de Correlacion: {r}')
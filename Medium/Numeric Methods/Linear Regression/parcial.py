import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 50, 100, 150, 200, 250])
y = np.array([0, 4, 8.3, 14, 17, 21])
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

resol = 100
xx = np.linspace(-2, 1000, resol)
yy = a0 + a1 * xx 

plt.scatter(x, y,label="Datos")
plt.plot(xx, yy, "r",label="Recta de regresión")
plt.xlabel("Tiempo (meses)")
plt.ylabel("Habitantes (Por Cien)")
plt.title("Gráfico de dispersión y recta de regresión")
plt.legend()
plt.grid()
plt.show()

y_mean = np.mean(y)

SST = np.sum((y - y_mean) ** 2)

y_est_vals = y_est(x)
SSR = np.sum((y_est_vals - y_mean) ** 2)

r=np.sqrt(SSR/SST)
print(f'Coeficiente de Correlacion: {r}')

# punto b:
matrix = np.array([
        [n, sum(x), sum(x ** 2)],
        [sum(x), sum(x ** 2), sum(x ** 3)],
        [sum(x ** 2), sum(x ** 3), sum(x ** 4)]
    ])

    
solutions = np.array([sum(y), sum(x * y), sum((x ** 2) * y)])

coefficients = np.linalg.solve(matrix, solutions)

a, b, c = coefficients

def y_est2(x):
    return a + b*x + c*(x**2)

print("Recta de Estimación")
print(f"Yest = {a} + {b}x + {c}x^2")

resol = 100
xx = np.linspace(-2, 10000, resol)
yy = a + b * xx + c * (xx ** 2)

plt.scatter(x, y,label="Datos")
plt.plot(xx, yy, "r",label="Recta de regresión")
plt.xlabel("Tiempo (meses)")
plt.ylabel("Habitantes (Por Cien)")
plt.title("Gráfico de dispersión y recta de regresión")
plt.legend()
plt.grid()
plt.show()

y_mean = np.mean(y)

SST = np.sum((y - y_mean) ** 2)

y_est_vals = y_est2(x)
SSR = np.sum((y_est_vals - y_mean) ** 2)

r=np.sqrt(SSR/SST)
print(f'Coeficiente de Correlacion: {r}')
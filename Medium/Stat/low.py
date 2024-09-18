# Reimportar librerías después del reinicio
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parámetros de la distribución
mu = 0 # Media
sigma_low = 1 # Desviación estándar baja (varianza baja)
sigma_high = 5  # Desviación estándar alta (varianza alta)

# Valores para el eje x
x = np.linspace(mu - 4 * sigma_high, mu + 4 * sigma_high, 1000)

# Funciones de densidad de probabilidad (curvas normales)
y_low = norm.pdf(x, mu, sigma_low)
y_high = norm.pdf(x, mu, sigma_high)

# Crear la gráfica
plt.figure(figsize=(10, 6))

# Curva para varianza baja
plt.plot(x, y_low, label=r'Varianza Baja: $\sigma^2 = 2^2$', color='blue')
plt.fill_between(x, y_low, color='blue', alpha=0.2)

# Curva para varianza alta
plt.plot(x, y_high, label=r'Varianza Alta: $\sigma^2 = 5^2$', color='green')
plt.fill_between(x, y_high, color='green', alpha=0.2)

# Líneas verticales en la media
plt.axvline(mu, color='red', linestyle='--', label=f"Media = {mu} cm")

# Títulos y etiquetas
plt.title("Distribución del Promedio Muestral con Varianzas Diferentes", fontsize=14)
plt.xlabel("Promedio Muestral (cm)", fontsize=12)
plt.ylabel("Densidad de Probabilidad", fontsize=12)

# Leyenda
plt.legend()

# Mostrar la cuadrícula
plt.grid(True)

# Mostrar la gráfica
plt.show()

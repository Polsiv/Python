import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# 1. Generación de datos sintéticos (ejemplo)
#    - Aquí deberías reemplazar con los datos reales si ya los tienes
# ------------------------------
def generar_datos_clase(figura, n=100, ruido=0.0):
    """
    Genera puntos 3D para una figura geométrica.
    figura: 'cubo', 'esfera', 'tetraedro'
    n: cantidad de puntos
    ruido: desviación estándar del ruido gaussiano
    """
    if figura == "cubo":
        datos = np.random.uniform(-1, 1, (n, 3))
    elif figura == "esfera":
        phi = np.random.uniform(0, np.pi, n)
        theta = np.random.uniform(0, 2*np.pi, n)
        r = 1
        x = r * np.sin(phi) * np.cos(theta)
        y = r * np.sin(phi) * np.sin(theta)
        z = r * np.cos(phi)
        datos = np.vstack((x, y, z)).T
    elif figura == "tetraedro":
        puntos = np.array([[1, 1, 1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1]])
        datos = puntos[np.random.randint(0, 4, n)] + np.random.normal(0, 0.1, (n, 3))
    else:
        raise ValueError("Figura no soportada")

    datos += np.random.normal(0, ruido, datos.shape)
    return datos

# ------------------------------
# 2. Perceptrón monocapa
# ------------------------------
class Perceptron:
    def __init__(self, n_inputs, lr=0.01):
        self.w = np.random.randn(n_inputs)
        self.b = np.random.randn()
        self.lr = lr

    def step(self, x):
        return np.where(x >= 0, 1, 0)

    def predict(self, X):
        return self.step(np.dot(X, self.w) + self.b)

    def train(self, X, y, epochs=100):
        errores = []
        for _ in range(epochs):
            total_error = 0
            for xi, yi in zip(X, y):
                y_hat = self.predict(xi)
                error = yi - y_hat
                self.w += self.lr * error * xi
                self.b += self.lr * error
                total_error += abs(error)
            errores.append(total_error)
        return errores

# ------------------------------
# 3. Ejemplo de uso
# ------------------------------
# Generar datos para dos clases separables
np.random.seed(42)
X_A = generar_datos_clase("esfera", n=50) + np.array([1.5, 1.5, 1.5])
X_B = generar_datos_clase("esfera", n=50) + np.array([-1.5, -1.5, -1.5])
y_A = np.ones(50)
y_B = np.zeros(50)

X = np.vstack((X_A, X_B))
y = np.hstack((y_A, y_B))

# Entrenar perceptrón
perceptron = Perceptron(n_inputs=3, lr=0.01)
errores = perceptron.train(X, y, epochs=50)

# ------------------------------
# 4. Graficar error por época
# ------------------------------
plt.plot(errores)
plt.xlabel("Épocas")
plt.ylabel("Errores totales")
plt.title("Evolución del error en entrenamiento")
plt.show()

# ------------------------------
# 5. Probar con datos ruidosos
# ------------------------------
X_ruido = X + np.random.normal(0, 0.2, X.shape)
pred_ruido = perceptron.predict(X_ruido)
precision = np.mean(pred_ruido == y)
print(f"Precisión con ruido: {precision*100:.2f}%")

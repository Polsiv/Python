import numpy as np

a = np.array([1.00, 2.00, 3.00])
a_barra = np.array([1.01, 1.99, 3.00])

norma_diferencia = np.linalg.norm(a - a_barra)
norma_a = np.linalg.norm(a)

error_relativo = norma_diferencia / norma_a

print("El error relativo es:", error_relativo)

import numpy as np
import matplotlib.pyplot as plt

def min_quad(x_data, y_data):

    n = len(x_data)

    matrix = np.array([
        [n, sum(x_data), sum(x_data ** 2)],
        [sum(x_data), sum(x_data ** 2), sum(x_data ** 3)],
        [sum(x_data ** 2), sum(x_data ** 3), sum(x_data ** 4)]
    ])

    
    solutions = np.array([sum(y_data), sum(x_data * y_data), sum((x_data ** 2) * y_data)])

    coefficients = np.linalg.solve(matrix, solutions)

    a, b, c = coefficients

    resol = 100
    xx = np.linspace(-2, 12, resol)
    yy = a + b * xx + c * (xx ** 2)

    _, ax = plt.subplots()
    ax.plot(xx, yy, 'r')
    ax.plot(x_data, y_data, 'o')
    plt.grid()
    plt.show()

x_data = np.array([1.1, 2.1, 3.01, 4, 4.98, 6.1, 7.02, 8, 9, 10])
y_data = np.array([4.1, 5.2, 12.2, 19, 31, 43, 52, 71, 84.6, 120])
min_quad(x_data, y_data)

import numpy as np

coefficent = np.array([[2, 1, -3],
                       [5 , -4, 1],
                       [1, -1, -4]])

solution = np.array([7, -19, 4])

print(np.linalg.solve(coefficent, solution))
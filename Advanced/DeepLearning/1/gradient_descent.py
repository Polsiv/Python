import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return 2 * x ** 2 + 3 * x * y + y ** 2 + 6

def gradient_of_f(x, y):
    df_dx = (4 * x) + (3 * y)
    df_dy = (3 * x) + (2 * y)
    return np.array([df_dx, df_dx])

def gradient_descent(starting_point, learning_rate = 0.01, max_iterations = 100, tolerance = 1e-6, verbose = False):
    point = np.array(starting_point, dtype = float)
    path = [point.copy()]

    for i in range(max_iterations):
        grad = gradient_of_f(*point)
        grad_norm = np.linalg.norm(grad)

        if verbose:
            print(f"Iter {i}: Point={point}, Gradient={grad}, Norm={grad_norm}")

        # stop if gradient is small enough
        if grad_norm < tolerance:
            if verbose:
                print(f"Converged in {i} iterations.")
            break

        point -= learning_rate * grad
        path.append(point.copy())

    return np.array(path)



def main(): 

    # run descent 
    start = (6, 6)
    path = gradient_descent(start, learning_rate = 0.05, max_iterations = 1000, verbose = True)

    # create grid
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    x, y = np.meshgrid(x, y)

    # function
    z = f(x, y)

    # create plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.plot_surface(x, y, z, cmap = 'viridis', edgecolors = 'none', alpha = 0.5)

    # plot path
    z_path = f(path[:,0], path[:,1])
    ax.plot(path[:,0], path[:,1], z_path, color = 'red', marker = 'o', label = "Gradient descent path")


    # labels
    ax.set_title('Surface of a Polynomial Function')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z = f(x, y)')

    plt.show()

if __name__ == "__main__":
    main()

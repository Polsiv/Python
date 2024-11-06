from vpython import box, vector, color
import numpy as np

def create_menger_sponge(level):
    
    """
    crea una esponja de menger de un nivel dado.
    args:
    level (int): el nivel de recursividad para la esponja de menger.
    returns:
    np.ndarray: ina matriz tridimensional que representa la esponja de menger.
    """
    
    size = 3 ** level  # tamaño del cubo en este nivel
    sponge = np.ones((size, size, size), dtype=int)  # inicializar la esponja con 1s (cubo literalemnte solido)


    def divide(x, y, z, size, level):
        
        """
        funcion recursiva que subdivide el cubo y elimina los subcubos centrales utilizando coordenadas (-1, 0, 1).
        args:
        x, y, z: las coordenadas actuales.
        size: el tamaño actual del cubo a subdividir.
        level: el nivel de profundidad actual en la recursión.
        """
        
        if level == 0:
            return  # caso base: no hacemos nada mas si llegamos al nivel 0

        # subcubos mas pequeños 
        new_size = size // 3

        # iterar sobre los 27 subcubos posibles en una cuadricula 3 x3 x3
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    # elimina el subcubo central en el medio y los subcubos centrales de cada cara y borde
                    if (i == 1 and j == 1) or (i == 1 and k == 1) or (j == 1 and k == 1):
                        
                        sponge[x + i * new_size:x + (i + 1) * new_size, 
                               y + j * new_size:y + (j + 1) * new_size, 
                               z + k * new_size:z + (k + 1) * new_size] = 0
                    else:
                        # llamada recursiva para subdividir los otros subcubos
                        divide(x + i * new_size, y + j * new_size, z + k * new_size, new_size, level - 1)

    # llamar a la funcion de division recursiva
    divide(0, 0, 0, size, level)


    return sponge

def draw_menger_sponge_vpython(level):
    """
    dibuja la esponja de Menger en 3D utilizando Vpython.
    args:
    level (int): nivel de la esponja de Menger.
    """
    # crear esponja de Menger como matriz 3D
    sponge = create_menger_sponge(level)
    size = sponge.shape[0]
    cube_size = 1  # Tamaño de cada cubo individual

    # iterar sobre los valores de la esponja y dibujar solo donde el valor sea 1
    for x in range(size):
        for y in range(size):
            for z in range(size):
                if sponge[x, y, z] == 1:
                    
                    # crear cubo en las coordenadas correspondientes
                    box(pos=vector(x * cube_size, y * cube_size, z * cube_size),
                        size=vector(cube_size, cube_size, cube_size),
                        color=color.cyan)


level = 3 
draw_menger_sponge_vpython(level)

while True:
    pass  # pa no cerrar la ventana
import numpy as np

def create_menger_sponge(level):
    size = 3 ** level
    sponge = np.ones((size, size, size), dtype=int)

    def divide(x, y, z, size, level):
        """
        x, y, z: Las coordenadas actuales.
        size: El tamaño actual del cubo a subdividir.
        level: El nivel de profundidad actual en la recursión.
        """
        if level == 0:
            return  # no hacemos nada más si llegamos al nivel 0

        # Tamaño de los subcubos más pequeños
        new_size = size // 3

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if (i == 1 and j == 1) or (i == 1 and k == 1) or (j == 1 and k == 1):
                        sponge[x + i * new_size:x + (i + 1) * new_size, 
                               y + j * new_size:y + (j + 1) * new_size, 
                               z + k * new_size:z + (k + 1) * new_size] = 0
                    else:
                        divide(x + i * new_size, y + j * new_size, z + k * new_size, new_size, level - 1)

    divide(0, 0, 0, size, level)
    return sponge

level = 2 
menger_sponge = create_menger_sponge(level)

print(f'Menger Sponge (Level {level}):\n', menger_sponge)
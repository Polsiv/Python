import numpy as np

def create_menger_sponge(level):
    """Creates a 3D array representing a Menger sponge."""
    # Size of the cube at the current level
    size = 3 ** level
    
    # Initialize a 3D array filled with 1s (solid cube)
    sponge = np.ones((size, size, size), dtype=int)
    
    def divide_and_conquer(x, y, z, size, level):
        if level == 0:
            return  # Base case, do nothing (sponge filled)
        
        # Calculate the size of the smaller cubes
        new_size = size // 3
        
        # Iterate through the 27 smaller cubes
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    # Skip the middle cube and the centers of each face
                    if (i == 1 and j == 1) and (k == 1):  # Center cube
                        sponge[x + i * new_size: x + (i + 1) * new_size,
                               y + j * new_size: y + (j + 1) * new_size,
                               z + k * new_size: z + (k + 1) * new_size] = 0
                    elif (i == 1 and j == 1) or (i == 1 and k == 1) or (j == 1 and k == 1):
                        sponge[x + i * new_size: x + (i + 1) * new_size,
                               y + j * new_size: y + (j + 1) * new_size,
                               z + k * new_size: z + (k + 1) * new_size] = 0
                    else:
                        divide_and_conquer(x + i * new_size, y + j * new_size, z + k * new_size, new_size, level - 1)

    # Start the recursive division
    divide_and_conquer(0, 0, 0, size, level)

    return sponge

# Example usage
level = 2  # Change this value for different levels of detail
menger_sponge = create_menger_sponge(level)

# Display the sponge shape
print(f'Menger Sponge (Level {level}):\n', menger_sponge)

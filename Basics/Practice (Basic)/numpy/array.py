import numpy as np

array = np.array([1, 2, 3, 4])
print(array)

# Multiplying by 2 each element of the array

array *= 2
print(array)

# Multiplying arrays

array2 = np.array([10, 20, 30, 40])
print(array * array2)

#new values for array
#range from 1-99, and 2000 values of em 
array = np.random.randint(1, 100, 2000)
array2 = np.random.randint(1, 100, 2000)

# Multiplying arrays
print (array2[1999])
print(array * array2)

#setting array back to the original values
array = np.array([1, 4, 9, 16, 25, 36])

print(f'Shape{array.shape}')
print(f'Powers:{array**2}')
print(f'Square root{np.sqrt(array)}')

#print each 2 elemnts
print(f'Square root{np.sqrt(array[::2])}')

#print each till n-element
print(f'Square root{np.sqrt(array[:2])}')

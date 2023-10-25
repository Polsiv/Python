import numpy as np

#<-------------------Basic matrices------------------------>

matrix = np.array([[1, 2], 
                  [3, 4]])
print(matrix)

matrix2 = np.array([[3, 4], 
                  [5, 6]])
print(matrix2)

#Adding to the matrix (escalares)
matrix += 100
print(matrix)

#Subtracting to the matrix (escalares)
matrix -= 100
print(matrix)

#Multiplying to the matrix (escalares)
matrix *= 5
print(f'Matrix multiplied by 5:{matrix}')



#<-------------------Broadcasting------------------------>

#product between vector and matric using broadcasting
x = np.array([3, 2])

#it takes x to multiply the matrix like 
#[3, 2], \n[3, 2]
print(f'Matrix multiplied by x:{matrix * x}')

#Using reshape to match the matrix shape
x2 = np.array([6, 7, 8, 9])
#print(f'Matrix 2 multiplied by x2 {matrix2 * x2}') # error
print(f'Matrix 2 by x2: {x2.reshape(2, 2) * matrix2}')


#<-------------------Multiplying matrices------------------------->

matrix3 = np.array([[10, 20],
                    [30, 40]])

matrix4 = np.array([[2, 4],
                    [6, 8]])
print(f'Matrix3 times matrix4 is equal to: {matrix3 * matrix4}')

#<-------------------Multiplying matrices (cross)------------------------->

print(f'Matrix3 times matrix4 (cross product) is equal to: {matrix3.dot(matrix4)}')

#<-------------------Transpose matrix------------------------->


print(f'Original matrix:\n{matrix3} \n Tranpose Matrix:\n {matrix3.T}')
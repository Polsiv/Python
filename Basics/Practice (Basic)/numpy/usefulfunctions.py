import numpy as np

#<-----------------Randint function---------------------->
#takes random numbers from -10 to 10 in a 5x5 matrix
notes = np.random.randint(-10, 11, (5, 5))
print(notes)

#<-----------------Max function--------------------->
print(np.max(notes))

#search by columns
print(np.max(notes, axis=0))

#search by raws
print(np.max(notes, axis=1))

#<-----------------Min function--------------------->
print(np.min(notes))

#search by columns
print(np.min(notes, axis=0))

#search by raws
print(np.min(notes, axis=1))

#<-----------------Std var--------------------->
#std is the same as taking the sqrt of var
print(np.std(notes))
print(np.var(notes))


#<-----------------Unique function--------------------->
#finds the values in the matrix, 
# but it displays them just once for each of em

print(np.unique(notes))
print(np.unique(notes, return_counts=True))

#<-----------------reshape-------------------->
randomMatrix = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

print(randomMatrix.reshape(2, 7))
print(notes.reshape(25))
#vector with 25 elements in it

#<-----------------dtype-------------------->
#this is numpy exclusive

print(notes.dtype)
print(randomMatrix.dtype)

#<-----------------Identity matrix-------------------->
#this is the same as multiplying by one, it doesnt affect
print(np.identity(5))
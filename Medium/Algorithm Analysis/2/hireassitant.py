import random

def randomize_in_place(arr: list):

    n = len(arr)
    for i in range(n):
        j = random.randint(i, n - 1)
        
        #Random swap
        arr[i], arr[j] = arr[j], arr[i]


list_1 = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
list_2 = [10, 8, 1, 3, 5, 2, 7, 4, 9, 6]
list_3 = [2, 1, 6, 3, 4, 5, 10, 7, 8, 8]

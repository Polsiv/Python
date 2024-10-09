import random

def randomize_in_place(arr: list):
    n = len(arr)
    for i in range(n):
        j = random.randint(i, n - 1)
        arr[i], arr[j] = arr[j], arr[i]


def randomized_hire_assistant(candidates: list):

    print(candidates)
    #Randon permutation
    randomize_in_place(candidates)

    print(candidates)
    best = 0  #Dummy Candidate
    for i in range(1, len(candidates)):
        if candidates[i] > best:
            best = candidates[i]
        
    #Returns the best candidate
    return best

    
print(randomized_hire_assistant([41, 2, 32, 33, 97, 30, 61, 1]))
def randomized_hire_assistant(candidates: list):

    #Randon permutation
    randomize_in_place(candidates)

    best = 0  #Dummy Candidate
    for i in range(1, len(candidates)):
        if candidates[i] > best:
            best = candidates[i]
        
    #Returns the best candidate
    return best


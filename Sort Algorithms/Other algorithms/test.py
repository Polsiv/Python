def countsort(list, max):
    list_count = [0] * (max + 1)
    list_sorted = [None]*len(list)
    
    for i in list:
        list_count[i]+=1
        print(list_count)
    
    total = 0
    for i in range(len(list_count)):
        list_count[i], total = total, total + list_count[i]
    
    for indice in list:
        list_sorted[list_count[indice]] = indice
        list_count[indice] +=1
        print(list_sorted)
    return list_sorted
           
oddlist = [9, 3, 1, 5, 9, 2, 0, 1]
countsort(oddlist, max(oddlist))

def quicksort(list, first, last):
    left = first
    right = last-1
    pivot = last
    while (left<right):
        while (list[left]<list[pivot]) and (left <=right):
            left +=1
        while (list[right]>list[pivot]) and (right >=left):
            right -=1
        if(left <right):
            list[left], list[right] = list[right], list[left]
            print(list)
    if(list[pivot]<list[left]):
            list[left], list[pivot] = list[pivot], list[left]
            print(list)
    if(first < left):
        quicksort(list, first, left-1)
    if(last>left):
        quicksort(list, left+1, last)
  
oddlist = [11, 3, 81, 7, 45]
quicksort(oddlist ,0 ,len(oddlist)-1)

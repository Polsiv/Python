def selection(list):
    for i in range(0,len(list)-1):
        min = i
        for j in range(i + 1, len(list)):
            if(list[j] < list[min]):
                min = j
        print(list)
        list[i], list[min] = list[min], list[i]

listodd = [11, 3, 81, 7, 45]
selection(listodd)
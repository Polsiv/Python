def inserction(list):
    for i in range(1, len(list) + 1):
        k = i - 1
        while(k > 0) and (list[k] < list[k - 1]):
            list[k], list[k - 1] = list[k - 1], list[k]
            k -= 1
        print(list)

listodd = [11, 3, 81, 7, 45]
inserction(listodd)
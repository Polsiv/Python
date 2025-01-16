def bubble_bidir(list):
    left = 0
    right = len(list)-1
    control = True

    while(left < right) and control:
        control = False
        for i in range(left, right):
            if(list[i] > list[i + 1]):
                control = True
                list[i], list[i + 1] = list[i  + 1], list[i]
                print(list)

        right -= 1  

        for j in range(right, left, -1):
            if(list[j] < list[j-1]):
                control = True
                list[j], list[j - 1] = list[j - 1], list[j]
                print(list)
        left += 1

oddList = [31, 33, 5, 87, 19, 49]
bubble_bidir(oddList)



        
            
            

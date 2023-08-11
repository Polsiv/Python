def betterBubble(list):
    i = 0
    control = True
    while(i <= len(list)-2 and control):
        control = False
        for j in range(0, len(list)-i-1):
            if(list[j] > list[j+1]):
                list[j], list[j + 1] = list[j+1], list[j]
                control = True
                print(list)
        i+=1        
      

list = [13, 3, 23, 43, 93, 73]
betterBubble(list)

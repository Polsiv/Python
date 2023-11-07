def month(days):

    day_of_week = [["M", "T", "W", "T", "F", "S", "S"], [], [], [], [], []]

    counter = 1
    for i in range(1, days + 1):
        
        if(len(day_of_week[counter]) < 7):
            day_of_week[counter].append(i)
        else:
            counter += 1

    for i in range(len(day_of_week)):
        for j in day_of_week[i]:
            print (j, end = " ")
        print()

    print(('{: > 2} '* 7).format(day_of_week))

month(30)
day = 1
daystarts = 0
for i in range(1, 31):
    if i == 1:
        print("   " * daystarts, end = "")
    print("{:>2}".format(i), end= " ")

    if(day + daystarts) % 7 == 0:
        print()
    day += 1

if day % 7 != 1:
    print()
print()
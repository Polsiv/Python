p1 = [0, 1]
p2 = [0, 1]

print(hex(id(p1)), hex(id(p2)))

if(p1 is p2):
    print("p1 and p2 pointers to the same dynamic variable")
else:
    print("p1 and p2 pointers to different dynamic variable")


d1 = {}
d2 = d1

print(id(d1), id(d2))

if(d1 is d2):
    print("d1 and d2 pointers to the same dynamic variable")
else:
    print("d1 and d2 pointers to different dynamic variable")



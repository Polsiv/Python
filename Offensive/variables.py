#!/usr/bin/env python3


#info that i always forget

mylist = [1,12, 12, 2, 4, 12, 5, 6]

#add 10 and 20
mylist.extend([10, 20])

# add 100 and 200
mylist += [100, 200]

print(sorted(mylist))

#print first 3 elements
print(mylist[:3])

#print since first 3 elements
print(mylist[3:])

#print first from 1st to 3rd element
print(mylist[1:4])

#print last element
print(mylist[-1])



#max and min value
max(mylist)
min(mylist)

#sum all
sum(mylist)

#insert hi to the 2nd position
mylist.insert(1, "hi")

#delete 1st element
del mylist[0]

#remove last element
mylist.pop()

#check index of the element
print(mylist.index(10))

print(mylist)

#enumerate returns both index and element
for i, j in enumerate(mylist):
    if j == 12:
        print(i, j, end= " : ")
        print(f"index: {i}")


#one liner

indices = [x for x, y in enumerate(mylist) if y == 12]


#count times element in list

print(mylist.count(12))

#remove repeated (ikhow to dot it)
new_list = set(mylist)
print(new_list)



#round float
print(round(1.213312, 2))


f = 12
s = 7

result = f ** s
print(result)
print("{:,}".format(result).replace(",", "."))

l1 = [1, 2, 3, 4, 6, 7]
l2 = [10, 20, 30, 40, 50, 60]

#sum of elements

result = list(map(sum, zip(l1, l2)))

for i in result:
    print(i)
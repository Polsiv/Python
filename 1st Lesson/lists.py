mylist = [3, 4, 10]
print(mylist)

#appending items

mylist.append(1)
print(mylist)

mylist.append(["Omg", "Appending", "NewItems?"])
print(mylist)

#removing items 

#removes the last item
mylist.pop()
print(mylist)

#swapping content

mylist[1] = 2
print(mylist)


#PRACTICE PROBLEM=========================================

fruits = ["banana", "apple", "mango"]

#swapping itmes, the last one with the first one

temp = fruits[0]

fruits[0] = fruits[2]
fruits[2] = temp
print(fruits)

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


print(list("ELPEPE"))

#turns string into a list   

mylist.insert(1,"fruio")

#enters value in specific index

mylist.extend("EL PEPE")
#turns the string into a list and appends it to the list

#del mylist[3] removes the index

copy_list = mylist.copy()
#creates an original copy of the list

#mylist.pop(index) removes the index
#my list.clear() clears the entire fucking list
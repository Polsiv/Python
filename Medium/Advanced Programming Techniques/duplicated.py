mystring = input("enter yyo word")

mystring = list(mystring)
mystring = sorted(mystring)
flag = False

for i in range(0, len(mystring) - 1):
    if mystring[i] == mystring[i + 1]:
        flag = True

print("found") if flag else print("not found")

#best case O(0), worst case O(n)

uniques = set(mystring)
if len(mystring) == len(uniques): print("elpepe")
else:print("la pepa")   
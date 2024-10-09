dic = {"hi": 1, "hi2": 2, "hi3": 3}

for hi, number in dic.items():
    print(number, hi)


for number in dic.values():
    print(number)

for hi in dic.keys():
    print(hi)


#comprehension list

odd_list = [1, 3, 5, 7, 9]

square = [i ** 2 for i in odd_list]

print(square)

#New stuf lol ========================

for i in range(5):
    print(i)

else: 
    print("for done")



for i in range(5):
    if i == 3:
        break

else: 
    #not printing since the break case performed
    print("for done")


#Same for while ========================
j = 0

while j > 10:
    print(j)
    j+=1

else:
    print("while success")

j = 0

while j < 10:

    if j == 5:
        break
    j+=1

else:
    print("while success")


k = 20

if 10 < k < 30:
    print("omg")


#ternary operator (god awful compared to c++)
msg = "youre!" if k != 20 else "lmao!"


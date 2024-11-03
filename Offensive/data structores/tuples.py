

#inmutables, insert, extend, remove, append

example = (1, 2, 3, 4, 5)

#first element ==== 

print(example[0])
print(example[-1])
print(example[1:3])


#Cant do this shit

#example[0] = 8

for i in example:
    print(i)

example


a, b, c, d, e = example

print(a, b, c, d, e)


#print lenght ===============
print(len(example))

# "modifying"
example2 = (10, 11, 12, 13)
example3 = example + example2
print(example3)
example4 = example * 4

eventuple = tuple(i for i in example3 if i % 2 == 0)
print(eventuple)

## REAL CASE SCENARIO =====================

db1_credential = ("silv", "xd123")

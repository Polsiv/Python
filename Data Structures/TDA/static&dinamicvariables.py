print("Static variables=============")
a = 10
b = a

print(id(b))
print(id(a))

print("====")

b = 15

print(id(b))
print(id(a))

print(a, b)

print("Dynamic variables=============")

l1 = [5, 10 ,15]
l2 = l1

l2[1] = 50
l2.append(150)

print(l1, l2)



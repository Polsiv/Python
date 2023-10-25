q = int(input("enter queries: "))

for i in range (q):
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    n = int(input("enter c: "))

    add = a

    for j in range(n):
        add += 2**j * b
        print(add, " ")

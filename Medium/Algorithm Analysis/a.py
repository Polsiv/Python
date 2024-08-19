target = 720
a = 1

for i in range(1, target + 1):
    a *= i
    if a == target:
        print(i)
        break
    elif a > target:
        break

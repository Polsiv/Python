#!/usr/bin/env python3


try:

    #print(3/0)
    omg = 3/2
    #print('hi'/2)
    int("HI")

except ZeroDivisionError as e:
    print("WHY DIVIDING BY 0 LMAO!??")
    print(e)

except (ZeroDivisionError , ValueError):
    print("lol")
    print("lol2")
else:
    print(omg)

finally:
    print("it always executes")


x = 1

if x < 0:
    raise Exception("Cant use negative numbers!")


lmao = "varibale = True"
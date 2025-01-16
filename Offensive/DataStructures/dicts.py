#!/usr/bin/env python3


dict = {"name": "silv", "age": 23, "island": "canarias"}


#iterate (keys is by default)
for i in dict:
    print(i)

#keys ("name")
for i in dict.keys():
    print(i)

# values (silv)
for i in dict.values():
    print(i)

# both
for i, j in dict.items():
    print(i, j)


#access key values

print(dict["name"])
print(dict["name"])

#access key by value
print(list(dict.keys())[list(dict.values()).index("silv")])

#change key values
dict["name"] = "pepega"

#delete key value

del dict["island"]
print(dict)


#check is key is present
if "name" in dict.keys():
    print(True)
else:
    print(False)


#get dict length
print(len(dict))


#wipe dict=========
#dict.clear()


#funny stuff
squares = {x: x ** 2 for x in range(10)}
print(squares)


#look for key value and print if not found

print(dict.get("name", "not found"))


#add more items

dict1 = {"name": "lmao"}
dict2 = {"age": 30}

dict1.update(dict2)

print(dict1)
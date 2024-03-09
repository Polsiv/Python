import re as r

password = "theres's nothing, nothing omg"

print(r.search("nothing", password).group())

print(r.findall("nothing", password))
print(r.split("\,", password))


password2 = "UUAjd322exf@"

#finds all the values from a to e
print(r.findall('[a-e]', password2))
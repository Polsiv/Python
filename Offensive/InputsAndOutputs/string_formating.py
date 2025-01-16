a = 1
b = 2

print("a + b = {0}".format(a + b))

text = "Hello world!"
#removes white spaces and tabulations from left and right handside
print(text.strip())

print(text.lower())
print(text.upper())
print(text.replace('o', 'x'))
new_text = text.split() #element for every white space
print(new_text)

text2 = "hello:world"
new_text2 = text2.split(":")
print(new_text2)

s = "Hello world!"

print("starts with H:", s.startswith("H"))
print("Is alpha:", s.isalpha())
print("Is digit:", s.isdigit())
print("Ends with !:", s.endswith("!"))
print("Find world", s.find("world")) # starts in position 6
print("Find adhs",  s.find("adhs")) #returns -1 if not found
print("Capitalize", s.capitalize())
print("Title", s.title())
print("Swapcase", s.swapcase())
print("Is lower", s.islower())
print("Is upper", s.isupper())
print("Is printable", s.isprintable())
# print(s.index('lol')) #raises exception if not found


counts = "test so we count the number of e's"
print("starts with H:", counts.count("e"))

to_remove = "from, bruh, to, huh"
removed = to_remove.replace(',', '')

table = str.maketrans('fmh', 'zpo')
new_removed = removed.translate(table)
print(new_removed)

string = ["Hello", "World"]
print(" ".join(string))
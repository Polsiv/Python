name = "silv" 

print(len(name))
#outputs 4

print(name.find(""))
#outputs the index if the the statement is found

print(name.capitalize())
#Silv

print(name.upper())
#SILV

print(name.lower())
#silv

print(name.isdigit())
#false, is not a number

print(name.isalpha())
#returns true if it only contains alphabetic letters

print(name.count("i"))
#counts the amount of letters within the array (1)

print(name.replace("i","u"))
#replaces content

print(name*3)
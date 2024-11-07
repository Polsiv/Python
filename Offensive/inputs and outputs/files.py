# exaple.txt

f = open("example.txt", "a")
f.write("Hello World")
f.close()

# another way

#closes the file automatically
with open("example.txt", "a") as f:
    f.write("HELLO WORLD \n")
    
    
with open("example.txt", "rb") as f:
    for line in f:
        print(line.strip())
    


with open("example.txt", "rb") as f: #rb raw binary
    #loads all the file in memory (not efficient)
    for line in f.readlines():
        print(line.strip().decode())
    

my_list = ["first\n", "second\n", "third\n", "fourth\n"]

with open("example.txt", "a") as f:
    f.writelines(my_list)
    
  
#no1 uses it
with open("test.txt", "w") as f:  
    print("omg hi there", file = f)
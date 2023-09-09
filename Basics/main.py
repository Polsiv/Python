imc = 0

weight = float(input("Enter ur weight"))
height = float(input("Enter ur height"))

imc = weight / height**2

print(imc)

if imc <= 15: 
    print("You are underweight")
else:
    if imc <= 25:
        print("You are normal weight")
    else:
        if imc <= 30:
            print("You are overweight")
            
dog = "coby"
comp = "cody andrey"

# while dog != comp:
#    dog = input("Enter the dogs name");
#    if dog == "Apollo":
#      continue
# if dog != comp:
#         print (f"{dog} is not the same as {comp}")
        
#While=========================================================

# status = False
# password = 1234 

# while not status: 
#     result = int(input("Enter the password"))
    

#for=========================================================

n = 10
listy = [1, 2, 3, 4, 1]
#for i in range(n):
    #print(i)

 

# for i in range(1, 11):
#     print (i)
    

# camino = ["thIS", "WORDS", "LOL"]

# for i in range(len(camino)):
#     print (camino[i], end="    ")

#for EACH=========================================================

for word in listy:
    print("Bruh")
    
tupla = (1, "hi", True)

interger, string, boolean = tupla
print (interger)
print(tupla)


#DICCIONARY

chars = {}


    
    
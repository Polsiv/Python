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
            
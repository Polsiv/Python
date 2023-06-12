import math

radius = float(input("Enter the radius: "))

if radius < 0:
    print("Invalid Input")
else:
    area = (radius**2) * math.pi
    print(f'the area is {area}')
    

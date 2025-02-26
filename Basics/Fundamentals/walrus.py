print(name := "elpepe")

#before
foods = []

# while True:
#     food = input("enter fav food")
#     if food == "exit":
#         break
#     foods.apend(food)

#after
    
while(food := input("enter fav food")) != "exit":
    foods.append(food)


    
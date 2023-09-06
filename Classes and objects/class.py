#https://www.youtube.com/watch?v=wfcWRAxRVBA Video explanation

class Robot:
    def __init__(self, name, color, weight):  #constructor

        self.name = name
        self.color = color
        self.weight = weight
    

    def introduce_self(self): #addint the argument self to every method I wanna add to the class
        print("My name is:  ",self.name) #self = this in java

#Robot 1-----(By using the default constructor)--------------------------------


# rl = Robot() #Robot() is the default py constructor
# rl.name = "Silv"
# rl.color = "Aqua"
# rl.weight = 25

# rl.introduce_self()

#Robot 2---------------(by using the new constructor)-----------------

rl = Robot("Silv", "aqua", 30)
r2 = Robot("Paul", "Red", 45)

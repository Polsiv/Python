import math

totalscores = int(input("Enter the amount of score you're going to evaluate: "))
scores = []
Tscore = 0
variation = 0 


for i in range (totalscores): 
   x = float(input("Enter the score: "))
   scores.append(x)
   Tscore += scores[i]
   variation += scores[i]**2
   
avg = Tscore/totalscores
variation/= totalscores

deviation = math.sqrt(variation)

print(f'The average is {avg} \n The variation is: {variation} \n The deviation is: {deviation}')
 


# for i in range(1, 22):
#   if (i % 5 == 0 and i % 3 == 0):
#     print(f'{i}:FizzBuzz')
#   elif (i % 5 == 0):
#     print(f'{i}:Buzz')
#   elif (i % 3 == 0):
#     print(f'{i}:Fizz')
#   else:
#     print(f'{i}:{i}')

#2 ifs
for i in range(1, 22):
  competedstring = ""
  if i % 3 == 0: competedstring += "Fizz"
  if i % 5 == 0: competedstring += "Buzz"
  print(i, competedstring or i)
  

#no ifs

for i in range (1, 22):
    competedstring = ""
    competedstring += "Fizz" * int(i % 3 == 0)
    competedstring += "Buzz" * int(i % 5 == 0)
    print(i, competedstring or i)


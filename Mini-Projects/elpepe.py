# for i in range(1, 22):
#   if (i % 5 == 0 and i % 3 == 0):
#     print(f'{i}:FizzBuzz')
#   elif (i % 5 == 0):
#     print(f'{i}:Buzz')
#   elif (i % 3 == 0):
#     print(f'{i}:Fizz')
#   else:
#     print(f'{i}:{i}')

# #after 
    
    
def calculator(n):

  fizz, Buzz = "Fizz", "Buzz"
  for i in range(1,     n + 1):
    toComplete = ""
    if (i % 3 == 0):
      toComplete += fizz
      print(i, toComplete)
      continue
    if (i % 5 == 0):
      toComplete += Buzz
      print(i, toComplete)
      continue
    print(i, i)


calculator(21)

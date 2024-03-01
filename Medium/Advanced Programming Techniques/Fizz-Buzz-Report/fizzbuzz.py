#5000 ifs

for i in range(1, 22):
  if (i % 5 == 0 and i % 3 == 0):
    print(f'{i}:FizzBuzz')
  elif (i % 5 == 0):
    print(f'{i}:Buzz')
  elif (i % 3 == 0):
    print(f'{i}:Fizz')
  else:
    print(f'{i}:{i}')

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


#from class
    
def read_from_file(filename):
    num_list = []
    with open(filename, "r") as f:
        content = f.read().splitlines()
    for i in content[1:101]:
        num_list.append(int(i))
    return (num_list)

def check(num_list):
    for i in num_list:
        completed_string = ""
        if i % 3 == 0: 
            completed_string += "Fizz"
        if i % 5 == 0: 
            completed_string += "Buzz"
        print(i, completed_string or i)

def main():
    my_list = read_from_file("input.txt")
    check(my_list)

main()


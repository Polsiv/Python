from weirdstringstack import *
import random as rd

pancakes = Pila()
x = rd.sample(range(1, 6), 5)
for i in x:
    apilar(pancakes, i)

sorted_stack = [1, 2, 3, 4, 5]

stack_to_sort = barrido_modificado(pancakes)
print(stack_to_sort)

while(sorted_stack != stack_to_sort):
    stack_to_sort, posicion_flip = act_flip(pancakes)
    print(stack_to_sort)
   # print(f'flip en la posicion: {posicion_flip}')
    


print(f'sorted stack: {stack_to_sort}')

    
    
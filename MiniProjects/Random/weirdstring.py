import random
from weirdstringstack import *

pancakes = Stack()
random_values = random.sample(range(1, 6), 5)
for value in random_values:
    push(pancakes, value)

sorted_stack = [1, 2, 3, 4, 5]

stack_to_sort = traverse_modified(pancakes)
print(stack_to_sort)

while sorted_stack != stack_to_sort:
    stack_to_sort, flip_position = act_flip(pancakes)
    print(stack_to_sort)
    # print(f' Position: {flip_position}')

print(f'Sorted stack: {stack_to_sort}')

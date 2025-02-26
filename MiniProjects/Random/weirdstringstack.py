import random

class StackNode:
    info, next = None, None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

def push(stack, data):
    node = StackNode()
    node.info = data
    node.next = stack.top
    stack.top = node
    stack.size += 1

def pop(stack):
    data = stack.top.info
    stack.top = stack.top.next
    stack.size -= 1
    return data

def is_empty(stack):
    return stack.top is None

def peek(stack):
    return stack.top.info if stack.top is not None else None

def get_size(stack):
    return stack.size

def traverse(stack):
    aux_stack = Stack()
    while not is_empty(stack):
        data = pop(stack)
        print(data)
        push(aux_stack, data)
    while not is_empty(aux_stack):
        data = pop(aux_stack)
        push(stack, data)

def traverse_modified(stack):
    traversed_list = []
    aux_stack = Stack()
    while not is_empty(stack):
        data = pop(stack)
        traversed_list.append(data)
        push(aux_stack, data)
    while not is_empty(aux_stack):
        data = pop(aux_stack)
        push(stack, data)
    return traversed_list

def act_flip(stack):
    flip_position = random.randint(2, 5)
    pos = 0
    temp_list = []
    while pos != flip_position:
        temp_list.append(pop(stack))
        pos += 1
    
    print(f'Flip at: {5 - flip_position}')
    for item in temp_list:
        push(stack, item)
    
    return traverse_modified(stack), (5 - flip_position)

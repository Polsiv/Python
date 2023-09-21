class stackNode(object):
    info, next = None, None

class MyStack(object):
    def __init__(self):
        self.top = None
        self.length = 0

#Basic funtions

def stacking(applestack, data):
    node = stackNode()
    node.info = data
    node.next = applestack.top
    applestack.top = node
    applestack.length += 1
    

def unstacking(applestack):
    x = applestack.top.info
    applestack.top = applestack.top.next
    applestack.length -= 1
    return x 

def empty_stack(applestack):
    return applestack.top is None

def on_top(applestack):
    if applestack.top is not None: return applestack.top.info
    else: return None

def stack_length(applestack):
    return applestack.length

def sweeping(applestack):
    stack_backup = MyStack()
    while(not empty_stack(applestack)):
        data = unstacking(applestack)
        print(data)
        stacking(stack_backup, data)

    while(not empty_stack(stack_backup)):
        data = unstacking(stack_backup)
        stacking(applestack, data)

#Problem functions

def find_range(applestack):
    stack_backup = MyStack()
    mini, maxi = 0, 0
    while(not empty_stack(applestack)):
        data = unstacking(applestack)
        if data < mini:
            mini = data
        if data > maxi:
            maxi = data
        stacking(stack_backup, data)

    while(not empty_stack(stack_backup)):
        data = unstacking(stack_backup)
        stacking(applestack, data)
    
    print(f'The range is from {mini}°C to {maxi}°C\nThe max value is: {maxi}°C, and the min value is: {mini}°C\n')

def find_average(applestack):
    stack_backup = MyStack()
    counter = 0

    while(not empty_stack(applestack)):
        data = unstacking(applestack)
        counter += data
        stacking(stack_backup, data)
    
    while(not empty_stack(stack_backup)):
        data = unstacking(stack_backup)
        stacking(applestack, data)

    average = counter / stack_length(applestack)
    return average

    
def below_and_above_temperatures(applestack):
    stack_backup = MyStack()
    belowavg, aboveavg = 0, 0
    average = find_average(applestack)

    while(not empty_stack(applestack)):
        data = unstacking(applestack)
        if data < average: belowavg += 1
        if data > average: aboveavg +=1
        stacking(stack_backup, data)

    while(not empty_stack(stack_backup)):
        data = unstacking(stack_backup)
        stacking(applestack, data)
    
    print(f'Days below mean: {belowavg} | Days above mean: {aboveavg}\n')

def switch_to_name(number):
    vehicles = {
    1: "Car",
    2: "Van",
    3: "Truck",
    4: "Bus"
    }
    return vehicles.get(number, -1)

class queueNode(object):
    info, nextnode = None, None

class Kiwi(object):
    def __init__(self):
        self.head, self.tail = None, None
        self.length = 0
    
#Checking fucntions
def empty_kiwi(queue):
    return queue.head is None

def in_front(queue):
    return queue.head.info

def length(queue):
    return queue.length

#Control functions
def appending(queue, data):
    node = queueNode()
    node.info = data
    if queue.head is None:
        queue.head = node
    else:
        queue.tail.nextnode = node
    queue.tail = node
    queue.length += 1

def attention(queue):
    data = queue.head.info
    queue.head = queue.head.nextnode
    if queue.head is None:
        queue.tail = None
    queue.length -= 1
    return data

def move_to_tail(queue):
    data = attention(queue)
    appending(queue, data)
    return data

def sweeping(queue):
    queue_backup = Kiwi()
    while(not empty_kiwi(queue)):
        data = attention(queue)
        print(data)
        appending(queue_backup, data)

    while(not empty_kiwi(queue_backup)):
        data = attention(queue_backup)
        appending(queue, data)
    
#Problem functions

def checking(queue):
    typeshit = {1: 47, 2: 59, 3: 71, 4: 64}
    data = queue.head.info
    queue.head = queue.head.nextnode
    if queue.head is None:
        queue.tail = None
    queue.length -= 1
    return typeshit[data]


def vehicle_type(queue):
    data = queue.head.info
    return switch_to_name(data)



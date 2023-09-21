class queueNode(object):
    info, nextnode = None, None

class Kiwi(object):
    def __init__(self):
        self.head, self.tail = None, None
        self.length = 0
    
def appending(queue, data):
    node = queueNode()
    node.info = data
    if queue.head is None:
        queue.head = node
    else:
        queue.tail.nextnode = node
    queue.tail = node
    queue.length += 1

def obtaining_data(queue):
    data = queue.head.info
    queue.head = queue.head.nextnode
    if queue.head is None:
        queue.tail = None
    queue.length -= 1
    return data
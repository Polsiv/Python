#Creating the element
class node(object):
    def __init__(self, data = None):
        self.data = data
        self.next = None

#Creating the head 
class linked_list:
    def __init__(self):
        self.head = node(
        )

#Appending new elements to the linked list
    def append(self, data):
        new_node = node(data)
        currently = self.head

        while currently.next != None:
            currently = currently.next
        currently.next = new_node
    
#Lenght function
    def length(self) -> int:
        currently = self.head
        total = 0
        while currently.next != None:
            total += 1
            currently = currently.next
        return total
    
#Display the current contents of our list
    def display(self):
        elements = []
        curnode = self.head
        while curnode.next != None:
            curnode = curnode.next
            elements.append(curnode.data)
        print (elements)


#Extracts the element we want
    def get(self, index):
        if index >= self.length():
            print ("Error: Index out of range.")
            return None
        
        curindex = 0
        curnode = self.head

        while True:
            curnode = curnode.next
            if curindex == index: return curnode.data
            curindex += 1

#Erase the elements from the list
    def erase(self, index):
        if index >= self.length(): 
            print("Erorr. index out of range.")
            return
        cur_idx = 0
        cur_node = self.head

        while True:
            last_node = cur_node
            cur_node = cur_node.next

            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1 


mylist = linked_list()


mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(6)

mylist.display()

print(mylist.get(1))

mylist.erase(2)
mylist.display()


 
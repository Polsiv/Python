#Creating the month(node)
class month: 
    def __init__(self, name = None, days = None):
        self.next = None
        self.name = name
        self.days = days 
       
#Creating the list (year 2023)
class linked_list:
    def __init__(self):
        self.head = month()
    
    def append(self, name, days):
        new_node = month(name, days)
        cur_node = self.head

        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node


#Display the elements
    def display(self):
        
        cur_node = self.head
    
        while cur_node.next != None:
            cur_node = cur_node.next

            test = []
            for i in range(1, cur_node.days + 1):
                test.append(i)

            print("Month:", cur_node.name, " Has: ", test)


months2023 = linked_list()
months2023.append("January", 31)
months2023.append("February", 28)
months2023.append("December", )
months2023.display()
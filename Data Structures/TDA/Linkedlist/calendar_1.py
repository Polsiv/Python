
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
    def display(self, daystarts):
        cur_node = self.head
        days_of_week = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
    
        while cur_node.next != None:
            cur_node = cur_node.next

            print(cur_node.name)
            print(" ".join(days_of_week))

            day = 1
            for i in range(1, cur_node.days + 1):
                if i == 1:
                    print("   " * daystarts, end = "")
                print("{:>2}".format(i), end= " ")

                if(day + daystarts) % 7 == 0:
                    print()
                day += 1

            if day % 7 != 1:
                print()
            print()
            daystarts = (daystarts + cur_node.days) % 7


months2023 = linked_list()
months2023.append("January", 31)
months2023.append("February", 28)
months2023.append("March", 31)
months2023.append("April", 30)
months2023.append("May", 31)
months2023.append("June", 30)
months2023.append("July", 31)
months2023.append("August", 31)
months2023.append("September", 30)
months2023.append("October", 31)
months2023.append("November", 30)
months2023.append("December", 31)
months2023.display(0)
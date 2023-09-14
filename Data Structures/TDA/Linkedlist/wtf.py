class Month: 
    def _init_(self, name=None, days=None):
        self.name = name
        self.days = days
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None
    
    def append(self, name, days):
        new_node = Month(name, days)
        if self.head is None:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = new_node

    def display(self, start_day):
        days_of_week = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.name)
            print(" ".join(days_of_week))
            day = 1
            for i in range(1, cur_node.days + 1):
                if i == 1:
                    print("   " * start_day, end="")
                print("{:>2}".format(i), end=" ")
                if (day + start_day) % 7 == 0:
                    print()
                day += 1
            if day % 7 != 1:
                print()
            print()
            start_day = (start_day + cur_node.days) % 7
            cur_node = cur_node.next

# Create a linked list of months
months = LinkedList()
months.append("January", 31)
months.append("February", 28)
months.append("March", 31)
months.append("April", 30)
months.append("May", 31)
months.append("June", 30)
months.append("July", 31)
months.append("August", 31)
months.append("September", 30)
months.append("October", 31)
months.append("November", 30)
months.append("December", 31)
months.display(0)
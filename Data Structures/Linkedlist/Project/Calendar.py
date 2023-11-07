from PIL import Image as img

#Calulating the lunar phase: https://saturncloud.io/blog/understanding-lunar-phases-a-guide-for-data-scientists/
def calculate_jdn(year, month, day):
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    jdn = day + ((153 * m + 2) // 5) + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    return jdn

def calculate_lunar_phase(jdn):
    new_moon_jdn = 2451550.1  # Known New Moon JDN, e.g., January 6, 2000
    lunar_cycle = 29.53  # Average length of a lunar cycle in days
    days_since_new_moon = jdn - new_moon_jdn
    lunar_phase = (days_since_new_moon % lunar_cycle) / lunar_cycle * 8
    rounded_phase = round(lunar_phase)
    return rounded_phase

#Setting up the months for the lunar phase
def switch_from_str_to_int(monthname):
    month_dict = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    return month_dict.get(monthname, -1)

#Creating the month(node)
class Month: 
    def __init__(self, name = None, days = 0):
        self.next = None
        self.name = name
        self.days = days 

        list = []
        for i in range(1, days + 1):
            list.append(i)
        self.listDay = list
        
#Creating the list (year 2023)
class Linked_list:
    def __init__(self):
        self.head = Month()
    
    def append(self, name, days):
        new_node = Month(name, days)
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

            print(" " * 5, cur_node.name)
            print(" ".join(days_of_week))
            day = 1

            for i in range(1, cur_node.days + 1):

                if i == 1: print("   " * daystarts, end = "")
                print("{:>2}".format(i), end= " ")
                if(day + daystarts) % 7 == 0:  print()
                day += 1
            print()
            daystarts = (daystarts + cur_node.days) % 7

#Calling the lunar phase function if the day and month given are found.
    def get(self, index, day):
        try:
            Phases = [{"LunarPhase": "New Moon", "Image": "NewMoon.png"},
            {"LunarPhase": "Waning Crescent", "Image": "WaningCrescent.png"},
            {"LunarPhase": "First Quarter", "Image": "FirstQuarter.png"},
            {"LunarPhase": "Waxing Gibbous", "Image": "WaxingGibbous.png"},
            {"LunarPhase": "Full Moon", "Image": "FullMoon.png"},
            {"LunarPhase": "Wanning Gibbous", "Image": "WaningGibbous.png"},
            {"LunarPhase": "Third Quarter", "Image": "ThirdQuarter.png"},
            {"LunarPhase": "Waning Crescent", "Image": "WaningCrescent.png"},
            {"LunarPhase": "New Moon", "Image": "NewMoon.png"}]

            cur_idx = 0
            cur_node = self.head
            while True:
                cur_node = cur_node.next
                if index == cur_node.name:
                    x = cur_node.name
                    jdn = calculate_jdn(2023, switch_from_str_to_int(x), cur_node.listDay[day - 1])
                    moon_img = img.open(Phases[calculate_lunar_phase(jdn)]["Image"])
                    moon_img.show()
                    return (f'On {cur_node.name} {cur_node.listDay[day - 1]}, The Moon phase was: {Phases[calculate_lunar_phase(jdn)]["LunarPhase"]}')

                cur_idx += 1
        except:
            return "Error, Either the month doesn't exist, or the day given is out of range."


#Appending new nodes(Months) to the Calendar(Linked list)
months2023 = Linked_list()
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

print(months2023.get("September", 28))


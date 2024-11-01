class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def work(self):
        raise NotImplementedError("")


class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size


    def work(self):
        return f"{self.name} manages a team of {self.team_size} and oversees projects."

class Developer(Employee):
    def __init__(self, name, salary, *programming_languages):
        super().__init__(name, salary)
        self.programming_languages = programming_languages


    def work(self):
        return f"{self.name} codes on {', '.join(self.programming_languages)} and gets paid {self.salary}"



paul = Developer("paul", 19999, "python", "c++", "bash")
julio = Manager("julio", 2, 9)


print(paul.work())
print(julio.work())

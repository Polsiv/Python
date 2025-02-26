#The Interface Segregation Principle (ISP) states that a class should not be forced to implement interfaces it does not use. This means creating smaller, specific interfaces instead of one large, general-purpose interface


from abc import ABC, abstractmethod

# Segregated interfaces
class Coder(ABC):
    @abstractmethod
    def code(self):
        pass

class Manager(ABC):
    @abstractmethod
    def manage(self):
        pass

# Implementing only relevant interfaces
class Developer(Coder):
    def code(self):
        print("Writing Python code...")

class TeamLead(Coder, Manager):
    def code(self):
        print("Reviewing code...")

    def manage(self):
        print("Managing the team...")

class ProjectManager(Manager):
    def manage(self):
        print("Planning the project...")

# Usage
dev = Developer()
dev.code()

lead = TeamLead()
lead.code()
lead.manage()

pm = ProjectManager()
pm.manage()


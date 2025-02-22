from abc import ABCMeta, abstractmethod

class Iperson(metaclass = ABCMeta):
   
    @staticmethod
    @abstractmethod
    def get_data():
        """implement this class"""
        
class SingletonPerson(Iperson):
    
    __instance = None
    
    @staticmethod
    def get_instance():
        if SingletonPerson.__instance == None:
            SingletonPerson("default", 0)
            
        return SingletonPerson.__instance
    
    def __init__(self, name, age):
        
        if SingletonPerson.__instance != None:
           return 
        
        self.name = name
        self.age = age
        SingletonPerson.__instance = self
        
    @staticmethod
    def get_data():
        return SingletonPerson.__instance.name, SingletonPerson.__instance.age
 
if __name__ == "__main__":
    p = SingletonPerson("silv", 20)
    print(p.get_data())
    p2 = SingletonPerson("bob", 25)
    print(p2.get_data())
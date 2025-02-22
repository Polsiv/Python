"""The same class behaves incorrectly in a multithreaded environment. 
Multiple threads can call the creation method simultaneously and get 
several instances of Singleton class."""

class SingletonMeta(type):
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class Singleton(metaclass = SingletonMeta):
    def business_logic(self):
        pass
    
if __name__ == "__main__":
    s1 = Singleton()
    s2 =  Singleton()
    
    print(id(s1) == id(s2))
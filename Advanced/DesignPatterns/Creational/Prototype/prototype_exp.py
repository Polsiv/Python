import copy

class Prototype:
    def clone(self):
        # Create a deep copy of the current instance
        return copy.copy(self)
    
class ConcretePrototype(Prototype):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.data = [x, y]
        
    def __str__(self):
        return f"ConcretePrototype(x={self.x}, y={self.y}, data={self.data})"
    
    
def main():

    original_object = ConcretePrototype(10, 20)
    cloned_object = original_object.clone()
    
    print("Original:", original_object)
    print("Cloned:  ", cloned_object)
    
    original_object.x = 30
    # the x stored in the cloned object doesnt change
    print("Cloned:  ", cloned_object)
    
main()
    
    
from abc import ABC, abstractmethod

class Notifier(ABC):
    """
    The base Component interface defines operations that can be altered by decorators.
    """
    @abstractmethod
    def send(self, mesage): 
        pass

class ConcretreNotifier(Notifier):
    """
    Concrete Components provide default implementations of the operations. There
    might be several variations of these classes.
    """
    
    def send(self, message) -> str:
        
        return f"Sending message: {message}"

class BaseDecorator(Notifier):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """
    
    _notifier: Notifier = None
    
    def __init__(self, wrappee: Notifier) -> None:
        
        self._notifier = wrappee

    @property
    def notifier(self) -> Notifier:
        
        return self._notifier

    def send(self, message) -> str:
        
        return self._notifier.send(message)

class EmailDecorator(BaseDecorator):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """
    
    def send(self, message) -> str:
        
        result = self.notifier.send(message)
        return f"{result}\nEmail sent: {message}"
    
class SMSDecorator(BaseDecorator):
    
    def send(self, message) -> str:
        
        result = self.notifier.send(message)
        return f"{result}\nSMS sent: {message}"


def client_code(notifier: Notifier) -> None:

    print(notifier.send("hi there!"))

if __name__ == "__main__":
    
    # Simple notifiaction
    simple_notifiacion = ConcretreNotifier()
    client_code(simple_notifiacion)
    
    # decorated notifications
    email = EmailDecorator(simple_notifiacion)
    sms = SMSDecorator(email)
    
    client_code(sms)
    

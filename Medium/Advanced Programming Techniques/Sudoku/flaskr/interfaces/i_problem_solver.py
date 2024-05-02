"""Module for the interface, providing abstract methods for our subclasses"""

from abc import abstractmethod, ABC

class IProblemSolver(ABC):
    """defines a contract that any class implementing it must follow"""
    
    @abstractmethod
    def compute_result(self, data):
        """method that computes and returns the result of the data given."""
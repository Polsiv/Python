from math import pi
from interfaces.i_probem_solver import IProblemSolver
from abc import abstractmethod

class Circle(IProblemSolver):
    
    def compute_results(self, data: float) -> list:
        calculations = {
            "diameter": self.diameter(data),
            "circumference": self.circumference(data),
            "area": self.area(data)
        }
        return [[key, value] for key, value in calculations.items()]

    @abstractmethod
    def diameter(self, data) -> float:
        return data * 2
    
    @abstractmethod
    def circumference(self, data) -> float:
        return data * 2 * pi
    
    @abstractmethod
    def area(self, data) -> float:
        return (data ** 2) * pi

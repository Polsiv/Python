from math import sqrt
from interfaces.i_probem_solver import IProblemSolver
from abc import abstractmethod

class Square(IProblemSolver):

    def compute_results(self, data):

        calculations = {
            "perimeter": self.perimeter(data),
            "area": self.area(data),
            "diagonals": self.diagonals(data),
            "inscribed circle": self.inscribed_circle(data)
        }

        return [[key, value] for key, value in calculations.items()]
    
    @abstractmethod
    def perimter(self, data):
        return data * 4
    
    @abstractmethod
    def area(self, data):
        return data ** 2
    
    @abstractmethod
    def diagonals(self, data):
        return sqrt(2) * data
    
    @abstractmethod
    def inscribed_circle(self, data):
        return (self.diagonals(data) / 2)

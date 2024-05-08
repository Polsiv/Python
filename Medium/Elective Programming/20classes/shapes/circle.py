from math import pi
from interfaces.i_problem_solver import IProblemSolver

class Circle(IProblemSolver):
    
    def compute_results(self, data) -> list:
        
        data = data[0]
        calculations = {
            "diameter": self.diameter(data),
            "circumference": self.circumference(data),
            "area": self.area(data)
        }
        return [[key, value] for key, value in calculations.items()]
    
    def diameter(self, data) -> float:
        return data * 2
    
    def circumference(self, data) -> float:
        return data * 2 * pi
    
    def area(self, data) -> float:
        return (data ** 2) * pi

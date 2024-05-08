from math import pow, sqrt
from interfaces.i_probem_solver import IProblemSolver

class Triangle(IProblemSolver):
    
    def compute_results(self, data) -> list:
        base = data[0]
        height = data[1]
        calculations = {
            "area": self.area(base, height),
            "perimeter": self.perimeter(base, height)
        }

        return [[key, value] for key, value in calculations.items()]

    def area(self, base, height) -> float:
        return base * height / 2
    
    def perimeter(self, base, height) -> float:
        return base + height + sqrt(pow(height, 2) + pow(height, 2))

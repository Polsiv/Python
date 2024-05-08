from interfaces.i_problem_solver import IProblemSolver
from math import pi, sqrt

class Ellipse(IProblemSolver):

    def compute_results(self, data):
        a, b = data[0], data[1] 
        calculations = {
            "area": self.area(a, b),
            "perimeter": self.perimeter(a, b)
        }
        return [[key, value] for key, value in calculations.items()]

    def area(self, a, b):
        return pi * a * b

    def perimeter(self, a, b):
        h = ((a - b) ** 2) / ((a + b) ** 2)
        return pi * (a + b) * (1 + (3 * h) / (10 + sqrt(4 - 3 * h)))

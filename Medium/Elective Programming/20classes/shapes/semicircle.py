from interfaces.i_problem_solver import IProblemSolver
from math import pi

class Semicircle(IProblemSolver):

    def compute_results(self, data):
        data = data[0]
        calculations = {
            "area": self.area(data),
            "perimeter": self.perimeter(data)
        }
        return [[key, value] for key, value in calculations.items()]

    def area(self, radius):
        return (pi * (radius ** 2)) / 2

    def perimeter(self, radius):
        return pi * radius + 2 * radius

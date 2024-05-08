from interfaces.i_problem_solver import IProblemSolver
from math import pi

class Oval(IProblemSolver):

    def compute_results(self, data):
        a, b = data[0], data[1]
        calculations = {
            "area": self.area(a, b)
        }
        return [[key, value] for key, value in calculations.items()]

    def area(self, a, b):
        return  pi * a * b
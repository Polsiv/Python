from interfaces.i_problem_solver import IProblemSolver
from math import tan, pi

class Pentagon(IProblemSolver):

    def compute_results(self, data):
        data = data[0]
        calculations = {
            "area": self.area(data)
        }
        return [[key, value] for key, value in calculations.items()]

    def area(self, side_length):
        return (5/4) * side_length ** 2 * (1 / tan(pi / 5))

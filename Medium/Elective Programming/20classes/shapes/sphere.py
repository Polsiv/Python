from interfaces.i_problem_solver import IProblemSolver
from math import pi

class Sphere(IProblemSolver):

    def compute_results(self, data):
        data = data[0]
        calculations = {
            "surface_area": self.surface_area(data),
            "volume": self.volume(data)
        }
        return [[key, value] for key, value in calculations.items()]

    def surface_area(self, radius):
        return 4 * pi * (radius ** 2)

    def volume(self, radius):
        return (4 / 3) * pi * (radius ** 3)

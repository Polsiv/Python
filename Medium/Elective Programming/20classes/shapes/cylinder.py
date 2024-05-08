from interfaces.i_problem_solver import IProblemSolver
from math import pi

class Cylinder(IProblemSolver):

    def compute_results(self, data):
        calculations = {
            "surface_area": self.surface_area(data),
            "volume": self.volume(data)
        }
        return [[key, value] for key, value in calculations.items()]

    def surface_area(self, data):
        radius, height = data[0], data[1]
        return 2 * pi * radius * (radius + height)

    def volume(self, data):
        radius, height = data[0], data[1]
        return pi * (radius ** 2) * height

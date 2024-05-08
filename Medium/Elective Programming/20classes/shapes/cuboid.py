from interfaces.i_problem_solver import IProblemSolver

class Cuboid(IProblemSolver):

    def compute_results(self, data):
        calculations = {
            "surface_area": self.surface_area(data),
            "volume": self.volume(data)
        }
        return [[key, value] for key, value in calculations.items()]

    def surface_area(self, data):
        length, width, height = data[0], data[1], data[2]
        return 2 * (length * width + length * height + width * height)

    def volume(self, data):
        length, width, height = data[0], data[1], data[2]
        return length * width * height

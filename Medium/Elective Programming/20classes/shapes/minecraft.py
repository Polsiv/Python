from interfaces.i_problem_solver import IProblemSolver

class Minecraft(IProblemSolver):

    def compute_results(self, data):
        data = data[0]
        calculations = {
            "surface_area": self.surface_area(data),
            "volume": self.volume(data)
        }
        return [[key, value] for key, value in calculations.items()]

    def surface_area(self, side_length):
        return 6 * (side_length ** 2)

    def volume(self, side_length):
        return side_length ** 3

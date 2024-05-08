from interfaces.i_probem_solver import IProblemSolver

class Rectangle(IProblemSolver):

    def compute_results(self, data):
        calculations = {
            "area": self.area(data),
            "perimeter": self.perimeter(data)
        }
        return [[key, value] for key, value in calculations.items()]

    def area(self, data):
        return data[0] * data[1]

    def perimeter(self, data):
        return 2 * (data[0] + data[1])


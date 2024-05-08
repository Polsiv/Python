from interfaces.i_problem_solver import IProblemSolver

class Rhombus(IProblemSolver):

    def compute_results(self, data):
        calculations = {
            "area": self.area(data)
        }
        return [[key, value] for key, value in calculations.items()]

    def area(self, data):
        diagonal1, diagonal2 = data[0], data[1]
        return (diagonal1 * diagonal2) / 2

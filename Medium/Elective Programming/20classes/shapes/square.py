from math import sqrt
from interfaces.i_problem_solver import IProblemSolver

class Square(IProblemSolver):

    def compute_results(self, data):
        data = data[0]

        calculations = {
            "perimeter": self.perimeter(data),
            "area": self.area(data),
            "diagonals": self.diagonals(data),
            "inscribed circle": self.inscribed_circle(data)
        }

        return [[key, value] for key, value in calculations.items()]
    
    def perimter(self, data):
        return data * 4
    
    def area(self, data):
        return data ** 2
    
    def diagonals(self, data):
        return sqrt(2) * data
    
    def inscribed_circle(self, data):
        return (self.diagonals(data) / 2)

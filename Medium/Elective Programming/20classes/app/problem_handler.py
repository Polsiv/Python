from interfaces.i_problem_solver import IProblemSolver

class ProblemHandler:
    def __init__(self, problem: IProblemSolver):
        self.problem =  problem
    
    def compute_results(self, data):
        return self.problem.compute_results(data)
        
from abc import ABC, abstractmethod
from .i_problem_solver import IProblemSolver

class ICreator(ABC):

    @abstractmethod
    def factory_method(self) -> IProblemSolver:
        pass

    def problem_to_solve(self, data):
        
        problem = self.factory_method()

        result = problem.compute_results(data)

        return result

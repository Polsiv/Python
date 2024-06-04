from .i_problem_creator import ICreator
from .i_problem_solver import IProblemSolver
from .prime_product import PrimeProduct

class PrimeCreator(ICreator):
    def factory_method(self) -> IProblemSolver:
        return PrimeProduct()
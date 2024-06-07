from .i_problem_creator import ICreator
from .i_problem_solver import IProblemSolver
from .fibonacci_product import FibonacciProduct

class FibonacciCreator(ICreator):

    def factory_method(self) -> IProblemSolver:
        return FibonacciProduct()

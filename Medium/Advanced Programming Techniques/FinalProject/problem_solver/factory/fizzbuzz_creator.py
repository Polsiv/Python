from .i_problem_creator import ICreator
from .i_problem_solver import IProblemSolver
from .fizzbuzz_product import FizzBuzz


class FizzBuzzCreator(ICreator):

    def factory_method(self) -> IProblemSolver:
        return FizzBuzz()
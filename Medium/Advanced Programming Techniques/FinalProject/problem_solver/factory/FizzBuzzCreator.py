from .ICreator import ICreator
from .Iproblem import IProblemSolver
from FizzBuzzProduct import FizzBuzz


class FizzBuzzCreator(ICreator):

    def factory_method(self) -> IProblemSolver:
        return FizzBuzz()
from ICreator import ICreator
from Iproblem import IProblemSolver
from PrimeProduct import PrimeProduct

class PrimeCreator(ICreator):
    def factory_method(self) -> IProblemSolver:
        return PrimeProduct()
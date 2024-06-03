from ICreator import ICreator
from Iproblem import IProblemSolver
from FibonacciProduct import FibonnaciProduct

class FibonacciCreator(ICreator):
    
    def factory_method(self) -> IProblemSolver:
        return FibonnaciProduct()
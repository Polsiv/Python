"""This module contains the evaluation of the number"""

from Interfaces.i_problem_solver import IProblemSolver

class FizzBuzz(IProblemSolver):
    """Fizz Buzz class"""

    def __init__(self) -> None:
        """Construct"""

    def compute_result(self, data):
        """returns the evaluation of any given integer"""
        competedstring = ""
        competedstring += "Fizz" * int(data % 3 == 0)
        competedstring += "Buzz" * int(data % 5 == 0)
        return competedstring or str(data)

#pylint: disable=R0903
"""This module contains the Problem Solver Interface"""

from abc import abstractmethod, ABC

class IProblemSolver(ABC):
    """Interface IproblemSolver"""

    @abstractmethod
    def compute_result(self, data):
        """Abstract method for computing results"""

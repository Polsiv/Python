from abc import ABC, abstractmethod

class IProblemSolver(ABC):
    @abstractmethod
    def compute_results(self, data):
        pass
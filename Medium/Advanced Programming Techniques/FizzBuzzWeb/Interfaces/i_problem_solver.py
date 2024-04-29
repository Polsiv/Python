from abc import abstractmethod, ABC

class IProblemSolver(ABC):

    @abstractmethod
    def compute_result(self, data):
        pass

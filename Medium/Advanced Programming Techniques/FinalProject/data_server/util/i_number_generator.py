
#pylint: disable = R0903, C0114
from abc import ABC, abstractmethod

class INumberGenerator(ABC):
    """Interface for generating numbers"""
    @abstractmethod
    def gen_numbers(self, low_limit, sup_limit, amount) -> list[int]:
        """abstract method for generating numbers"""

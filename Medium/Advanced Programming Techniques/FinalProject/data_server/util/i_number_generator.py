from abc import ABC, abstractmethod

class INumberGenerator(ABC):
    
    @abstractmethod
    def gen_numbers(self, low_limit, sup_limit, amount) -> list[int]:
        pass
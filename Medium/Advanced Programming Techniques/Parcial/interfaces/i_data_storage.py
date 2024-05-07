
from abc import ABC, abstractmethod

class IDataStorage(ABC):
    @abstractmethod
    def save_data(self, data):
        pass

    @abstractmethod
    def read_data(self):
        pass

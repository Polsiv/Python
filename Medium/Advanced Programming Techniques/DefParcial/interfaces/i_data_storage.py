
from abc import ABC, abstractmethod

class IDataStorage(ABC):
    @abstractmethod
    def save_data(self, path, data):
        pass

    @abstractmethod
    def read_data(self):
        pass

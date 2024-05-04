from abc import ABC, abstractmethod

class IDataStorage(ABC):
    @abstractmethod
    def read_data(self):
        pass
    
    def save_data(self, data):
        pass
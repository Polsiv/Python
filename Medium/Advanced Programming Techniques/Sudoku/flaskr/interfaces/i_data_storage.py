"""this module provides the method for getting the input from the .txt file"""

from abc import ABC, abstractmethod

class IDataStorage(ABC):
    """defines the for the storage classes"""

    @abstractmethod
    def read_data(self):
        """reads the data and returns it"""

    @abstractmethod
    def save_data(self, data):
        """stores the data"""
from abc import ABC, abstractmethod

class IDataStorage(ABC):

    @abstractmethod
    def post_data(self, data):
        pass

    @abstractmethod
    def get_data(self, data):
        pass
    
    @abstractmethod
    def get_active_data(self, data):
        pass

    @abstractmethod
    def delete_data(self, data):
        pass

    @abstractmethod
    def get_range(self, low_limit, sup_limit):
        pass


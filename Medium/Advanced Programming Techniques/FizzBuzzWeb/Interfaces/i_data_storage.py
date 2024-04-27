from abc import ABC, abstractmethod

class IDataStorage(ABC):

    @abstractmethod
    def post_data():
        pass

    @abstractmethod
    def get_data():
        pass
    
    @abstractmethod
    def delete_data():
        pass
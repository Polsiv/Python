"""This module contains the data storage interface"""
from abc import ABC, abstractmethod

class IDataStorage(ABC):
    """Interface Data Storage"""

    @abstractmethod
    def post_data(self, data):
        """Abstract method for posting data"""

    @abstractmethod
    def get_data(self, data):
        """Abstract method for getting data"""

    @abstractmethod
    def get_active_data(self, data):
        """Abstract method for getting active data"""

    @abstractmethod
    def delete_data(self, data):
        """Abstract method for deleting data"""

    @abstractmethod
    def get_range(self, low_limit, sup_limit):
        """Abstract method for getting range"""

    @abstractmethod
    def update_inactive_data(self, data):
        """Abstract method for deleting data"""

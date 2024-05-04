from interfaces.i_data_storage import IDataStorage

class DataHandler:
    def __init__(self, storage: IDataStorage):
        self.storage = storage

    def save_data(self, path, data):
        self.storage.save_data(path, data)

    def read_data(self, path):
        return self.storage.read_data(path)
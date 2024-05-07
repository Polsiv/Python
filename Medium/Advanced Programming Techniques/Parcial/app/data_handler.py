from interfaces.i_data_storage import IDataStorage

class DataHandler:
    def __init__(self, storage: IDataStorage):
        self.storage = storage

    def save_data(self, data):
        self.storage.save_data(data)

    def read_data(self):
        return self.storage.read_data()
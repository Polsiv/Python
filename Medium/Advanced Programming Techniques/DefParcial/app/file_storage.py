import json
from typing import List
from interfaces.i_data_storage import IDataStorage

class FileStorage(IDataStorage):
    def __init__(self, config_file_path):

        with open(config_file_path, 'r') as config_file:
            config = json.load(config_file)
            self.input_path = config['input_path']
            self.output_path = config['output_path']

    def save_data(self, data):

        with open(self.output_path, "w") as f:
            for i in data:
                f.write(f'{i[0]} {i[1]}\n')
            f.close()

    def read_data(self):
            
            with open(self.input_path, 'r', encoding="utf-8") as f:
                lines = f.readlines()
                num = int(lines[0])
                data = []
                for i in lines[2:2+num]:
                    data.append(int(i))
            return data


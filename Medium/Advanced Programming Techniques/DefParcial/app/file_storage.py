import json
import sys
from interfaces.i_data_storage import IDataStorage

class FileStorage(IDataStorage):
    def __init__(self, config_file_path):

        with open(config_file_path, 'r') as config_file:
            config = json.load(config_file)
            self.input_path = config['input_path']
            self.output_path = config['output_path']
            self.filename = config["name"]

    def save_data(self, data):

        with open(self.output_path, "w") as f:
            for i in data:
                f.write(f'{i[0]} {i[1]}\n')
            print(f'{self.filename} output file generated.')
            f.close()

    def read_data(self):
        
        try: 
            with open(self.input_path, 'r', encoding="utf-8") as f:
                lines = f.readlines()
                num = int(lines[0])
                data = []
                for i in lines[2:2+num]:
                    data.append(i)
            return data
        
        except (ValueError, IndexError) as e:
            print(e)
            sys.exit()

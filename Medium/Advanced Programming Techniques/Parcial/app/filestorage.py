from interfaces.i_data_storage import IDataStorage
class FileStorage(IDataStorage):

    def read_data(self, filename):
        with open(filename, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            num = int(lines[0])
            data = []
            for i in lines[2:]:
                data.append(int(i))
        return num, data

    def save_data(self, filename, data):
        with open(filename, "w") as f:
            f.write(f"{data[0]}\n")
            f.write(f"\n")
            for i in data[1]:
                f.write(f'{i[1]} {i[0]}\n')
            f.close()
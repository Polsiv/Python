from .db_storage import DBStorage

class MyApp:
    def __init__(self) -> None:
        self.storage = DBStorage()

    def get_number(self, number):
        db_result = self.storage.get_data(number)
        if db_result is None:
            return "Not Found", 404
        else:
            return f'{db_result[0]}: {db_result[1]}', 200


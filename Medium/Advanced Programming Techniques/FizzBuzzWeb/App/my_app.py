from .db_storage import DBStorage
from .fizz_buzz import FizzBuzz

class MyApp:

    def __init__(self) -> None:
        self.storage = DBStorage()
        self.fizzbuzz = FizzBuzz()

    def get_number(self, number):
        db_result = self.storage.get_data(number)
        if db_result is None:
            return "Not Found", 404
        else:
            return f'{db_result[0]}: {db_result[1]}', 200

    def post_number(self, number):
        db_active_result = self.storage.get_active_data(number)
        db_result = self.storage.get_data(number)
        
        if db_active_result is None:

            if db_result is None:
                self.storage.post_data([number, self.fizzbuzz.compute_result(number)])
                return f'{number}: {self.fizzbuzz.compute_result(number)}', 201
            
            else: 
                self.storage.update_inactive_data(number)
                return f'{db_result[0]}: {db_result[1]}', 200
            
        else: return f'{db_result[0]}: {db_result[1]}', 409
    

    def get_range(self, low_limit, sup_limit):
        db_result = self.storage.get_range(low_limit, sup_limit)
        if low_limit > sup_limit:
            return "error at stablishing limits.", 400
            
        else: 
            if len(db_result) == 0: 
                return "Not Found.", 404
            
            else:
                nums_dict = {}
                for row in db_result:
                    nums_dict[str(row[0])] = row[1]
                return nums_dict, 200

    def delete_number(self, number): 
        db_result = self.storage.get_active_data(number) 
        if db_result is None:
            return "Not Found.", 404
        else:
            self.storage.delete_data(number)
            return "", 204
            
        

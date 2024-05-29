"""This module contains the API logic that returns the retrieved data and the HTTP code"""
from .db_storage import DBStorage
from .fizz_buzz import FizzBuzz
from Interfaces.i_data_storage import IDataStorage
from Interfaces.i_problem_solver import IProblemSolver

class MyApp:
    """class my app"""

    def __init__(self) -> None:
        """constructor"""
        self.storage:IDataStorage = DBStorage()
        self.fizzbuzz:IProblemSolver = FizzBuzz()

    def get_number(self, number):
        """logic to get specific number"""
        db_result = self.storage.get_data(number)
        db_result_active = self.storage.get_active_data(number)
        if db_result is None or db_result_active is None:
            return "Not Found", 404

        return f'{db_result[0]}: {db_result[1]}', 200

    def post_number(self, number):
        """logic to post a number"""
        db_active_result = self.storage.get_active_data(number)
        db_result = self.storage.get_data(number)

        if db_active_result is None:
            if db_result is None:
                self.storage.post_data([number, self.fizzbuzz.compute_result(number)])
                return f'{number}: {self.fizzbuzz.compute_result(number)}', 201

            self.storage.update_inactive_data(number)
            return f'{db_result[0]}: {db_result[1]}', 200

        return f'{db_result[0]}: {db_result[1]}', 409

    def get_range(self, low_limit, sup_limit):
        """logic to get the range"""
        db_result = self.storage.get_range(low_limit, sup_limit)
        if low_limit > sup_limit:
            return "error at stablishing limits.", 400

        if len(db_result) == 0:
            return "Not Found.", 404

        nums_dict = {}
        for row in db_result:
            nums_dict[str(row[0])] = row[1]
        return nums_dict, 200

    def delete_number(self, number):
        """logic to soft-delete a number"""
        db_result = self.storage.get_active_data(number)
        if db_result is None:
            return "Not Found.", 404

        self.storage.delete_data(number)
        return "", 204
    
    def hard_delete_number(self, number):
        """logic to hard-delete a number"""
        db_result = self.storage.get_data(number)
        if db_result is None:
            return "Not Found.", 404
        
        self.storage.hard_delete_data(number)
        return "", 204

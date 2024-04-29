from Interfaces.i_data_storage import IDataStorage
import sqlite3
from DataBase.initialdatabase import data_base_route

class DBStorage(IDataStorage):
    def __init__(self):
        pass

    @staticmethod   
    def db_connection():
        connection = sqlite3.connect(".\DataBase\database.db")
        connection.row_factory = sqlite3.Row
        return connection
    
    def get_active_data(self, data):
        connection = self.db_connection()
        with connection:
            cursor = connection.cursor()
            result = cursor.execute("SELECT num, num_evaluated FROM numbers WHERE num = ? AND active = '1'", (data,)).fetchone()
        connection.close()
        return result
        
    def get_data(self, data):
        connection = self.db_connection()
        with connection:
            cursor = connection.cursor()
            result = cursor.execute("SELECT num, num_evaluated FROM numbers WHERE num = ?", (data,)).fetchone()
        connection.close()
        return result
    
    def post_data(self, data):
        connetion = self.db_connection() 
        with connetion:
            cursor = connetion.cursor()
            cursor.execute("INSERT INTO numbers (num, num_evaluated, active) VALUES (?, ?, 1)", (data[0], data[1]))
        connetion.commit()
        connetion.close()
        return 
        
    def update_inactive_data(self, data):
        connection = self.db_connection()
        with connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE numbers SET active = '1' WHERE num = ?", (data,))
        connection.commit()
        connection.close()
        return
    

    def get_range(self, low_limit, sup_limit):
        connection = self.db_connection()
        with connection:
            cursor = connection.cursor()
            results = cursor.execute("SELECT * FROM NUMBERS WHERE num BETWEEN ? AND ? AND active = '1'", (low_limit, sup_limit)).fetchall()
        connection.close()
        return results
 
    def delete_data(self, data):
        connection = self.db_connection()
        with connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE numbers SET active = '0' WHERE num = ?", (data,))
        connection.commit()
        connection.close()
        return
    

    
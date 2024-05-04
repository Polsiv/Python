"""
This module contains the the logic for the sql queries that retrieves
our data
"""
import sqlite3
from Interfaces.i_data_storage import IDataStorage
from DataBase.initialdatabase import DATA_BASE_ROUTE

class DBStorage(IDataStorage):
    """
    Data Base Storage class
    """
    def __init__(self):
        """
        Constructor
        """

    @staticmethod
    def db_connection():
        """
        Stablish connection,
        """
        connection = sqlite3.connect(DATA_BASE_ROUTE)
        connection.row_factory = sqlite3.Row
        return connection

    def get_active_data(self, data):
        """
        Query for active data
        """
        connection = self.db_connection()
        with connection:
            cursor = connection.cursor()
            result = cursor.execute("SELECT num, num_evaluated FROM numbers WHERE num = ? AND active = '1'",
                                    (data,)).fetchone()
        connection.close()
        return result

    def get_data(self, data):
        """
        Query for non-active data
        """
        connection = self.db_connection()
        with connection:
            cursor = connection.cursor()
            result = cursor.execute("SELECT num, num_evaluated FROM numbers WHERE num = ?", (data,)).fetchone()
        connection.close()
        return result

    def post_data(self, data):
        """
        Query for posting data
        """
        connetion = self.db_connection()
        with connetion:
            cursor = connetion.cursor()
            cursor.execute("INSERT INTO numbers (num, num_evaluated, active) VALUES (?, ?, 1)",
                           (data[0], data[1]))
        connetion.commit()
        connetion.close()

    def update_inactive_data(self, data):
        """
        Query for updating inactive data
        """
        connection = self.db_connection()
        with connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE numbers SET active = '1' WHERE num = ?", (data,))
        connection.commit()
        connection.close()

    def get_range(self, low_limit, sup_limit):
        """
        Query for getting the range
        """
        connection = self.db_connection()
        with connection:
            cursor = connection.cursor()
            results = cursor.execute("SELECT * FROM NUMBERS WHERE num BETWEEN ? AND ? AND active = '1'",
                                    (low_limit, sup_limit)).fetchall()
        connection.close()
        return results

    def delete_data(self, data):
        """
        Query for deleting the data
        """
        connection = self.db_connection()
        with connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE numbers SET active = '0' WHERE num = ?", (data,))
        connection.commit()
        connection.close()

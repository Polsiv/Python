import sqlite3 
from test import *


data_base_name = "database.db"
connection = sqlite3.connect(data_base_name)
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS numbers (
              number_id INTEGER PRIMARY KEY,
              number INTEGER, 
              number_evaluated TEXT,
              active INTEGER
            )
    """)

def get_data():
    
    data_from_input = read_from_file("input.txt")

    data = []
    for i in data_from_input:
        data.append((i, i, check_numbers(i), 1))   
  
    return data

def insert_data():
    data = get_data() 
    
    cursor.executemany("INSERT INTO numbers (number_id, number, number_evaluated, active) VALUES (?, ?, ?, ?)", data)
    connection.commit()


def print_data():
    sql_statement = "SELECT * FROM numbers"
    for row in cursor.execute(sql_statement):
        print(row)


insert_data()
print_data()

connection.close()

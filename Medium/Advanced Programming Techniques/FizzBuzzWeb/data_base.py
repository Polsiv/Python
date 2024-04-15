import sqlite3 
import pandas as pd

data_base_name = "database.db"
connection = sqlite3.connect(data_base_name)
cursor = connection.cursor()
schema_file = "schema.sql"

def execute_schema():
    with open(schema_file) as file:
        connection.executescript(file.read())

def test_data(filename):
    data = []
    try:
        with open(filename, encoding='utf-8') as f:
            for i in f:
                parts = i.strip().split()
                
                data.append((int(parts[0]), parts[1], True))             
        return data
    except FileNotFoundError:
        return None

def insert_data():
    file_name =  "input.txt"
    data = test_data(file_name)
    
    cursor.executemany("INSERT INTO numbers (num, num_evaluated, active) VALUES (?, ?, ?)", data)
    connection.commit()

def print_data():
    df = pd.read_sql_query("SELECT * FROM numbers", connection)
    print(df)

#execute_schema()
#insert_data()
#print_data()
connection.close()

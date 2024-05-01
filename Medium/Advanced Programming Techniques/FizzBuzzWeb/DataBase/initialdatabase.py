"""This module creates the initial state of the data base"""

import sqlite3
import pandas as pd

DATA_BASE_NAME = "database.db"
CONNECTION = sqlite3.connect(DATA_BASE_NAME)
CURSOR = CONNECTION.cursor()
SCHEMA_FILE = "schema.sql"
DATA_BASE_ROUTE = ".\DataBase\database.db"

def execute_schema():
    """executes the schema"""
    with open(SCHEMA_FILE) as file:
        CONNECTION.executescript(file.read())

def test_data(filename):
    """reads the input file"""
    data = []
    try:
        with open(filename, encoding = "utf-8") as f:
            for i in f:
                parts = i.strip().split()

                data.append((int(parts[0]), parts[1], True))
        return data
    except FileNotFoundError:
        return None

def insert_data():
    """inserts the new data"""
    file_name =  "input.txt"
    data = test_data(file_name)

    CURSOR.executemany("INSERT INTO numbers (num, num_evaluated, active) VALUES (?, ?, ?)", data)
    CONNECTION.commit()

def print_data():
    """prints the data"""
    df = pd.read_sql_query("SELECT * FROM numbers", CONNECTION)
    print(df)

#execute_schema()
#insert_data()
#print_data()
CONNECTION.close()

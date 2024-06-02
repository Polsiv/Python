#pylint: disable=W1401
#pylint: disable=W1514
"""This module creates the initial state of the data base"""

import sqlite3
import uuid
import pandas as pd
from werkzeug.security import generate_password_hash

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

def root_data(filename):
    """reads the input file for root data"""
    try:
        with open(filename, encoding = "utf-8") as f:
            data = f.readlines()
            data = [line.strip() for line in data]
            return  data
    except FileNotFoundError:
        return None

def insert_root():
    """insert root into the database"""

    data = root_data("rootuser.txt")
    username = data[0]
    password = data[1]
    public_id = str(uuid.uuid4())
    hashed = generate_password_hash(password, method = 'pbkdf2:sha256')
    CONNECTION.execute("INSERT INTO users (public_id, username, u_password) VALUES  (?, ?, ?)",
                       (public_id, username, hashed))
    CONNECTION.commit()

def print_data():
    """prints the data"""
    df = pd.read_sql_query("SELECT * FROM numbers", CONNECTION)
    print(df)

#execute_schema()
#insert_data()
#insert_root()
#print_data()
CONNECTION.close()

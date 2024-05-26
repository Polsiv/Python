import sqlite3
from flask_bcrypt import bcrypt
from os import getenv
import pandas as pd


DATA_BASE_NAME = "userdatabase.db"
CONNECTION = sqlite3.connect(DATA_BASE_NAME)
SCHEMA_FILE = "users.sql"



def test_data(filename):
    """reads the input file"""
    try:
        with open(filename, encoding = "utf-8") as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        return None


def execute_schema():
    with open(SCHEMA_FILE) as file:
        CONNECTION.executescript(file.read())

def insert_root():
    data = test_data("rootuser.txt")

    username = data[0]
    password = data[1]
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    CONNECTION.execute("INSERT INTO users (username, pass, u_root) VALUES  (?, ?, 1)", (username, hashed))
    
    CONNECTION.commit()
    

def print_data():
    """prints the data"""
    df = pd.read_sql_query("SELECT * FROM users", CONNECTION)
    print(df)


#execute_schema()
#insert_root()
#print_data()
CONNECTION.close()

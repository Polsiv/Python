import sqlite3

DATA_BASE_NAME = "userdatabase.db"
CONNECTION = sqlite3.connect(DATA_BASE_NAME)
SCHEMA_FILE = "users.sql"

def execute_schema():
    with open(SCHEMA_FILE) as file:
        CONNECTION.executescript(file.read())

def insert_root():
    CONNECTION.execute("INSERT INTO users (username)")
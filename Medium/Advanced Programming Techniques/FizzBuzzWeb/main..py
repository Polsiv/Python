import sqlite3
from flask import Flask
import data_base

app = Flask(__name__)

@app.route('/')
def index():
    return "omg hi :3"


app.run(host = "0.0.0.0", port = 81)
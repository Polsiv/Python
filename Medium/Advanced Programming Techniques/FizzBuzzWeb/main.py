import sqlite3
from flask import Flask, jsonify, request   
import data_base, fizz_buzz

def data_base_connection():
    connection = sqlite3.connect(data_base.data_base_name)
    connection.row_factory = sqlite3.Row
    return connection

def number_in_data_base(num):
    connection = data_base_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM numbers WHERE num = ?', (num,))
    count = cursor.fetchone()[0]
    connection.close()
    return count > 0
    
app = Flask(__name__)

@app.route('/')
def index():
    return "Home"

#GET
@app.route('/numbers/', methods=['GET'])
def numbers_get():
    connection = data_base_connection()
    number = request.args.get('num')
    cursor = connection.cursor()

    cursor.execute('SELECT num, num_evaluated FROM numbers WHERE num = ?', (number,))
    result = cursor.fetchone()
    if result is not None:
        return f'{result[0]}: {result[1]}'
    else:
        return "Number not found.", 404
        
#POST
@app.route('/numbers/', methods=['POST'])
def numbers_post():
    connection = data_base_connection()
    number = request.get_json()["num"]
    cursor = connection.cursor()
    evaluated_number = fizz_buzz.check_numbers(number)
    
    if number_in_data_base(number): 
        return "number already in data base", 405
    else:
        cursor.execute("INSERT INTO numbers (num, num_evaluated, active) VALUES (?, ?, ?)", (number, evaluated_number, True))
        connection.commit()
        connection.close()
        return f'{number} has been added with success.', 201

#DELETE
@app.route('/numbers/', methods = ['DELETE'])
def numbers_delete():
    connection = data_base_connection()
    cursor = connection.cursor()
    number = request.args.get("num")

    if number_in_data_base(number):
        cursor.execute("DELETE FROM numbers where num = ?", (number,))
        connection.commit()
        connection.close()
        return f'{number} deleted with success.', 200
    else:
        return 'Number not found.', 404
    
#GET RANGE
@app.route('/numbers/range', methods = ['POST'])
def numbers_range():
    connection = data_base_connection()
    cursor = connection.cursor()
    limits = request.get_json()
    low_limit = limits["lowlimit"]
    sup_limit = limits["suplimit"]

    if low_limit > sup_limit:
        return "limits are not well defined", 400
    else:
        cursor.execute('SELECT * FROM NUMBERS WHERE num BETWEEN ? AND ?', (low_limit, sup_limit))
        numbers = cursor.fetchall()
        results = [dict(row) for row in numbers]
        return jsonify(results), 200
        
#GET FOR ALL NUMBERS
@app.route('/numbers', methods=['GET'])
def numbers_getall():
    connection = data_base_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM numbers')
    fizz_buzz_numbers = cursor.fetchall()
    connection.close()
    
    results = [dict(row) for row in fizz_buzz_numbers]
    return jsonify(results), 200

  

app.run(host = "0.0.0.0", port = 80)
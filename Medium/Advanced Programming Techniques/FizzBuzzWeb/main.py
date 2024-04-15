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
    cursor.execute("SELECT COUNT(*) FROM numbers WHERE num = ?", (num,))
    count = cursor.fetchone()[0]
    return count > 0
        
app = Flask(__name__)

@app.route('/')
def index():
    return "Home"

#GET
@app.route('/numbers/', methods=['GET'])
def numbers_get():
    number = request.args.get('num')
    connection = data_base_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT num, num_evaluated FROM numbers WHERE num = ? AND active = '1'", (number,))
    result = cursor.fetchone()
    connection.close()
    if result is not None:
        return f'{result[0]}: {result[1]}'
    else:
        return "Number not found, or may be disabled", 404
        
#POST
@app.route('/numbers/', methods=['POST'])
def numbers_post():
    connection = data_base_connection()
    cursor = connection.cursor()
    number = request.get_json()["num"]
    evaluated_number = fizz_buzz.check_numbers(number)
    
    if number_in_data_base(number): 
        connection.close()
        return "number already in data base (if not show it should be disabled)", 405
    else:
        cursor.execute("INSERT INTO numbers (num, num_evaluated, active) VALUES (?, ?, ?)", (number, evaluated_number, True))
        connection.commit()
        connection.close()
        return f'{number} has been added with success.', 201

#REMOVE AND RETRIEVE
@app.route('/numbers/', methods = ['PUT'])
def numbers_delete():
    connection = data_base_connection()
    cursor = connection.cursor()
    number = request.get_json()["num"]
    enable = request.get_json()["enable"]

    if number_in_data_base(number):
        cursor.execute('UPDATE numbers SET active = ? WHERE num = ?', (enable, number))
        connection.commit()
        connection.close()
        return f'{number}, disabled with success.', 200
    
    else: 
        connection.close()
        return 'Number not found or may be already disabled.', 404
    
    
#GET RANGE
@app.route('/numbers/range', methods = ['POST'])
def numbers_range():
    connection = data_base_connection()
    cursor = connection.cursor()
    limits = request.get_json()
    low_limit = limits["lowlimit"]
    sup_limit = limits["suplimit"]

    if low_limit > sup_limit:
        connection.close()
        return "limits are not well defined", 400
    else:
        cursor.execute("SELECT * FROM NUMBERS WHERE num BETWEEN ? AND ? AND active = '1'", (low_limit, sup_limit))
        numbers = cursor.fetchall()
        connection.close()
        results = [dict(row) for row in numbers]
        return jsonify(results), 200
    
        
#GET FOR ALL NUMBERS
@app.route('/numbers', methods=['GET'])
def numbers_getall():
    connection = data_base_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM numbers WHERE active = '1'")
    fizz_buzz_numbers = cursor.fetchall()    
    results = [dict(row) for row in fizz_buzz_numbers]
    connection.close()
    return jsonify(results), 200

    
app.run(host = "0.0.0.0", port = 80)
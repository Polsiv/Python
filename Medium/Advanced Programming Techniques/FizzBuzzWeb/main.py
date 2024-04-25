import sqlite3
from flask import Flask, jsonify, request   
import database
from fiiz_buzz import check_numbers

def data_base_connection():
    connection = sqlite3.connect(database.data_base_name)
    connection.row_factory = sqlite3.Row
    return connection

def number_in_db(num):
    connection = data_base_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM numbers WHERE num = ?", (num,))
    count = cursor.fetchone()[0]
    return count > 0

def number_active(num):
    connection = data_base_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM numbers WHERE num = ? and active = '1' ", (num,))
    count = cursor.fetchone()[0]
    return count > 0
 
app = Flask(__name__)

#POST
@app.route('/numbers/', methods=['POST'])
def numbers_post():
    connection = data_base_connection()
    cursor = connection.cursor()
    number = request.args.get('num')
    
    if number_in_db(number):  
        cursor.execute("SELECT num, num_evaluated FROM numbers WHERE num = ?", (number,))
        result = cursor.fetchone()
        connection.close()
        return f'{result[0]}: {result[1]}', 409
    
    if number_in_db(number) and not number_active(number):
        cursor.execute("UPDATE numbers SET active = '1' WHERE num = ?", (number,))
        connection.commit()
        cursor.execute("SELECT num, num_evaluated FROM numbers WHERE num = ?", (number,))
        result = cursor.fetchone()
        connection.close()
        return f'{result[0]}: {result[1]}', 200

    if not number_in_db(number):
        evaluated_number = check_numbers(int(number))
        cursor.execute("INSERT INTO numbers (num, num_evaluated, active) VALUES (?, ?, ?)", (number, evaluated_number, 1))
        cursor.execute("SELECT num, num_evaluated FROM numbers WHERE num = ?", (number,))
        result = cursor.fetchone()
        connection.commit()
        connection.close()
        return f'{check_numbers(int(number))}', 201

#REMOVE
@app.route('/numbers/', methods = ['DELETE'])
def numbers_delete():
    connection = data_base_connection()
    cursor = connection.cursor()
    number = request.args.get("num")
    if number_in_db(number) and number_active(number):   
        cursor.execute("UPDATE numbers SET active = '0' WHERE num = ?", (number,))
        connection.commit()
        connection.close()
        return f'{number}, deleted.', 200
    
    else: 
        connection.close()
        return 'Number not found or may be already disabled.', 404

#GET
@app.route('/numbers/', methods=['GET'])
def numbers_get():
    number = request.args.get('num')
    connection = data_base_connection()
    cursor = connection.cursor()
    
    if number_in_db(number):
        cursor.execute("SELECT num, num_evaluated FROM numbers WHERE num = ?", (number,))
        result = cursor.fetchone()
        connection.close()
        return f'{result[0]}: {result[1]}', 200
        
    else:
        connection.close()
        return "Number not found.", 404


app.run(host = "0.0.0.0", port = 80)

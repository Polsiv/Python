"""
This is the main module
"""
from flask import Flask, request
from App.my_app import MyApp

app = Flask(__name__)
my_app = MyApp()

@app.route('/numbers/<number>', methods = ['GET', 'POST', 'DELETE'])
def numbers(number):
    """this is where we will get our data from Postman"""
    try:
        if request.method == "GET":
            return my_app.get_number(int(number))

        if request.method == "POST":
            return my_app.post_number(int(number))

        if request.method == "DELETE":
            return my_app.delete_number(int(number))

    except ValueError:
        return "Invalid input.", 400

@app.route('/range/', methods = ['POST'])
def get_range():
    """this is where we will get our data from Postman"""
    try:
        limits = request.get_json()
        low_limit = limits["lowlimit"]
        sup_limit = limits["suplimit"]
        return my_app.get_range(int(low_limit), int(sup_limit))

    except ValueError:
        return "Invalid input.", 400

app.run(host = "0.0.0.0", port = 80)

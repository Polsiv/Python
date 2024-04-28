from flask import Flask, jsonify, request
from App.my_app import MyApp

app = Flask(__name__)

my_app = MyApp()

@app.route('/numbers/<number>', methods = ['GET, POST, DELETE'])
def numbersn(number):

    if request.method == "GET":
        return my_app.get_number(number)
    
    if request.method == "POST":
        return


app.run(host = "0.0.0.0", port = 80)

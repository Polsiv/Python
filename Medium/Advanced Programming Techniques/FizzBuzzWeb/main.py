from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/numbers/', methods = ['GET'])
def numbers():
    return "Hello World", 200


app.run(host = "0.0.0.0", port = 80)

"""
This is the main module
"""

from App.users import Users
from flask import Flask, request, jsonify
from App.my_app import MyApp
from functools import wraps
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd404516c04f243109e4b94197d3b61fc'
my_app = MyApp()
users = Users()

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'access-token' in request.headers:
            token = request.headers['access-token']
            print(token)

        if not token:
            return jsonify({'message': 'Token is missing!'}, 401)

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms = ['HS256'])
            current_user = users.get_user(data['public_id'])

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 403        

        return f(current_user, *args, **kwargs)

    return decorated    


@app.route('/login')
def login():
    auth = request.authorization
    return users.login_user(auth, app.config['SECRET_KEY'])
   

@app.route('/register', methods = ['POST'])
def register():
    data = request.get_json()
    return users.register_user(data)
    
@app.route('/numbers/<number>', methods = ['GET', 'POST', 'DELETE'])
@token_required
def numbers(current_user, number):
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
@token_required
def get_range(current_user):
    """this is where we will get our data from Postman"""
    try:
        limits = request.get_json()
        low_limit = limits["lowlimit"]
        sup_limit = limits["suplimit"]
        return my_app.get_range(int(low_limit), int(sup_limit))

    except ValueError:
        return "Invalid input.", 400

app.run(host = "0.0.0.0", port = 80, debug = True)

"""
This is the main module
"""

from App.userhandler import UserHandler
from flask import Flask, request
from App.my_app import MyApp
from flask_jwt_extended import JWTManager, jwt_required, get_jwt
from datetime import timedelta
import redis

app = Flask(__name__)
my_app = MyApp()
userhandler = UserHandler()
jwt = JWTManager(app)
app.config['SECRET_KEY'] = 'd404516c04f243109e4b94197d3b61fc'
ACCESS_EXPIRES = timedelta(minutes=15)

jwt_redis_blocklist = redis.StrictRedis(
    host="localhost", port=6379, db=0, decode_responses=True
)

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    token_in_redis = jwt_redis_blocklist.get(jti)
    return token_in_redis is not None


@app.route('/register', methods = ['POST'])
def register():
    data = request.get_json()
    return userhandler.register_user(data)

@app.route('/login')
def login():
    auth = request.authorization
    return userhandler.login_user(auth)
   
@app.route('/logout', methods = ['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    return userhandler.logout_user(jti, ACCESS_EXPIRES, jwt_redis_blocklist)

@app.route('/numbers/<number>', methods = ['GET', 'POST', 'DELETE'])
@jwt_required()
def numbers(number):
    current_user = get_jwt()
    """this is where we will get our data from Postman"""
    try:
        if request.method == "GET":
            return my_app.get_number(int(number))

        if request.method == "POST":
            return my_app.post_number(int(number))

        if request.method == "DELETE":
            if current_user['root'] == 1:
                return my_app.hard_delete_number(int(number))
            
            return my_app.delete_number(int(number))

    except ValueError:
        return "Invalid input.", 400

@app.route('/range/', methods = ['POST'])
@jwt_required()
def get_range():
    """this is where we will get our data from Postman"""
    try:
        limits = request.get_json()
        low_limit = limits["lowlimit"]
        sup_limit = limits["suplimit"]
        return my_app.get_range(int(low_limit), int(sup_limit))

    except ValueError:
        return "Invalid input.", 400

app.run(host = "0.0.0.0", port = 80, debug = True)

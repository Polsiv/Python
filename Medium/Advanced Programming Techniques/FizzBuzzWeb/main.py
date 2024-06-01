from flask import Flask, request, jsonify, render_template
from App.userhandler import UserHandler
from App.my_app import MyApp
from flask_jwt_extended import JWTManager, jwt_required, get_jwt, get_jwt_identity
from datetime import timedelta
import redis
import logging


app = Flask(__name__)
my_app = MyApp()
userhandler = UserHandler()
jwt = JWTManager(app)
app.config['SECRET_KEY'] = 'd404516c04f243109e4b94197d3b61fc'
ACCESS_EXPIRES = timedelta(minutes=20)
logging.basicConfig(level=logging.DEBUG)


jwt_redis_blocklist = redis.StrictRedis(
    host="localhost", port=6379, db=0, decode_responses=True
)

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    token_in_redis = jwt_redis_blocklist.get(jti)
    return token_in_redis is not None

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return userhandler.register_user(data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    data = request.get_json()
    
    return userhandler.login_user(data)

@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    return userhandler.logout_user(jti, ACCESS_EXPIRES, jwt_redis_blocklist)

@app.route('/numbers/<int:number>', methods=['GET', 'POST', 'DELETE'])
@jwt_required()
def numbers(number):

    logging.debug('Request Headers: %s', request.headers)
    authorization_header = request.headers.get('Authorization')
    print("huh ",authorization_header)
    logging.debug('Authorization Header: %s', authorization_header)
                  
    current_user = get_jwt_identity()
    try:
        if request.method == "GET":
            return my_app.get_number(number)
        if request.method == "POST":
            return my_app.post_number(number)
        if request.method == "DELETE":
            if current_user['root'] == 1:
                return my_app.hard_delete_number(number)
            return my_app.delete_number(number)
    except ValueError:
        return "Invalid input.", 400

@app.route('/range/', methods=['POST'])
@jwt_required()
def get_range():
    try:
        limits = request.get_json()
        low_limit = limits["lowlimit"]
        sup_limit = limits["suplimit"]
        return my_app.get_range(int(low_limit), int(sup_limit))
    except ValueError:
        return "Invalid input.", 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)

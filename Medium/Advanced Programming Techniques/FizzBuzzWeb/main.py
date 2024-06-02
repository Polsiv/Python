import functools
from flask import Flask, request, jsonify, render_template, session, redirect
from App.userhandler import UserHandler
from App.my_app import MyApp
from flask_jwt_extended import JWTManager
from datetime import timedelta
import redis
import jwt as pyjwt
from jwt import ExpiredSignatureError, InvalidTokenError

app = Flask(__name__)
my_app = MyApp()
userhandler = UserHandler()
jwt = JWTManager(app)
app.config['SECRET_KEY'] = 'd404516c04f243109e4b94197d3b61fc'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes = 10)

ACCESS_EXPIRES = timedelta(minutes = 5)

def jwt_required_custom(endpoint=None):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            token = session.get('token')
            if not token:
                return jsonify({"msg": "Missing token"}), 401
            try:
                data = pyjwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            except ExpiredSignatureError:
                return jsonify({"msg": "Token has expired"}), 401
            except InvalidTokenError:
                return jsonify({"msg": "Invalid token"}), 401
            except Exception:
                return jsonify({"msg": "Token decoding error"}), 401

            return fn(*args, **kwargs)
        return wrapper
    
    if endpoint:
        return decorator
    return decorator

#for redis
jwt_redis_blocklist = redis.StrictRedis(
    host="localhost", port=6379, db=0, decode_responses=True
)

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    token_in_redis = jwt_redis_blocklist.get(jti)
    return token_in_redis is not None

#normal routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = str(request.form.get('username'))
        password = str(request.form.get('password'))
        data = {'username': username, 'password': password}
        result_db = userhandler.register_user(data)

        if result_db['message'] == "user already created!":
            return render_template('/signup.html', message =result_db)

        return render_template('login.html', message = result_db) 
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = str(request.form.get('username'))
        password = str(request.form.get('password'))
        infouser = {"username": username, "password": password}
        msg = userhandler.login_user(infouser)

        if msg['message'] != "Invalid Password" and  msg['message'] != "User not registered":
            session['username'] = infouser['username']
            session['token'] = msg['message']
            return redirect('/numbers')
        return render_template('login.html', message = msg)
    return render_template('login.html')

@app.route('/logout', methods=['POST'])
@jwt_required_custom(endpoint='logout_endpoint')
def logout():
    token = session.get('token')
    session.pop('token')
    session.pop('username')
    result = userhandler.logout_user(token, ACCESS_EXPIRES, jwt_redis_blocklist)['message']
    return render_template('index.html', message = result)

@app.route('/numbers', methods=['GET', 'POST', 'DELETE'])
@jwt_required_custom(endpoint='numbers_endpoint')
def numbers():
    current_user = session.get('username')
    try:
        if request.method == "GET":
            number = request.args.get('number_get')
            if not number:
                return render_template('numbers.html', current_user = current_user)
            result = my_app.get_number(int(number))
            return render_template('numbers.html', current_user = current_user, get_result = result)
        
        if request.method == "POST":
            if request.form.get('_method') == 'DELETE':

                number = request.form.get('number_delete')
                if current_user == "root":
                    result = my_app.hard_delete_number(int(number))
                    return render_template('numbers.html', current_user = current_user, delete_result = result)
                
                result = my_app.delete_number(int(number))
                return render_template('numbers.html', current_user = current_user, delete_result = result)

            number = request.form.get('number_post')

            result = my_app.post_number(int(number))
            return render_template('numbers.html', current_user = current_user, post_result = result)
    
    except ValueError:
        return "Invalid input.", 400

@app.route('/range/', methods=['GET', 'POST'])
@jwt_required_custom(endpoint='range_endpoint')
def get_range():

    if request.method == 'POST':
        try:
            low_limit= str(request.form.get('lowLimitInput'))
            sup_limit= str(request.form.get('supLimitInput'))
            result = my_app.get_range(int(low_limit), int(sup_limit))
            return render_template('range.html', num_range = result)
        
        except ValueError:
            return "Invalid input.", 400
    return render_template('range.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)

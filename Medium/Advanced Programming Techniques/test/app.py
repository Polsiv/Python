from flask import Flask, jsonify, make_response, render_template, request, session
import jwt
from datetime import datetime, timedelta
from functools import wraps

import jwt.exceptions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'p\xbf\x86f\x10\x8a\xa6\xffG^\x18\xe8'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'Alert': 'Token is missing!'}), 403
        
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms = ['HS256'])
        
        except jwt.ExpiredSignatureError:
            return jsonify({'Alert': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'Alert': 'Invalid Token!'}), 403
        
        return f(*args, **kwargs)
    
    return decorated

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    return "logged in"

@app.route('/login', methods = ['POST'])
def login():
   
    if request.form['username'] and request.form['password'] == '12345':
        session['logged_in'] = True

        token = jwt.encode({
            'user':request.form['username'],
            'expiration': str(datetime.now() + timedelta(seconds = 12))
            }, 
            app.config['SECRET_KEY'], algorithm = "HS256")

        print(type(token))
        return jsonify({'token': token})
    
    return make_response('Unable to Verify', 403, {'WWW-Authenticate': 'Basic realm: "Authentication falied!'})
        
@app.route('/public')
def public():
    return 'For Public'


@app.route('/auth')
@token_required
def auth():
    'JWT verified!'

if __name__ == "__main__":
    app.run(debug=True)

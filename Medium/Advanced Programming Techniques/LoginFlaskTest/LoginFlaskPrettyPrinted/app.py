from flask import Flask, jsonify, request, make_response
import jwt
import datetime
from functools import wraps
"""this is just a basic example"""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b7a078fb25f842b788adc528e1f59e29'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        print("token",token)
        if not token:
            return jsonify({'message': 'Token is mising!'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except:
            return({'message': 'invalid'}), 403
        
        return f(*args, **kwargs)
    
    return decorated

@app.route('/unprotected')
def unproctected():
    return jsonify({'message': 'anyone can view this'})


@app.route('/protected')
@token_required
def protected():
    return jsonify({'message': 'only people with token can view this'})


@app.route('/login')
def login():

    auth = request.authorization

    if auth and auth.password == "pas123":
        exp_time = datetime.datetime.now() + datetime.timedelta(minutes = 1 )
        exp_time_timestamp = int(exp_time.timestamp())
        token = jwt.encode({'user': auth.username, 'exp': exp_time_timestamp}, app.config['SECRET_KEY'])

        return jsonify({'token': token})

    return make_response('could not verify!', 401, {'WWW-Authenticate': 'Basic Realm = "Login Required"'})
    

if __name__ == '__main__':
    app.run(debug = True)
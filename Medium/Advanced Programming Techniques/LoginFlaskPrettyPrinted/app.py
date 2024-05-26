from flask import Flask, jsonify, request, make_response
import jwt
from datetime import datetime,timedelta
"""this is just a basic example"""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b7a078fb25f842b788adc528e1f59e29'

@app.route('/unprotected')
def unproctected():
    return ''


@app.route('/protected')
def protected():
    return ''

@app.route('/login')
def login():

    auth = request.authorization

    if auth and auth.password == "password":
        token = jwt.encode({'user': auth.username, 'exp': datetime.now() + timedelta(minutes=30)}, 'b7a078fb25f842b788adc528e1f59e29')

        return jsonify({'token': token})


    return make_response('could not verify!', 401, {'WWW-Authenticate': 'Basic Realm = "Login Required"'})
    

if __name__ == '__main__':
    app.run(debug = True)
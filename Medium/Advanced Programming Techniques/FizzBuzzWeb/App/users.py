import sqlite3
import uuid
from flask import jsonify, make_response
from DataBase.initialdatabase import DATA_BASE_ROUTE
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

class Users():

    token_black_list = set()

    @staticmethod
    def db_connection():
        connection = sqlite3.connect(DATA_BASE_ROUTE)
        connection.row_factory = sqlite3.Row
        return connection
    
    def get_user(self, username):
        connection = self.db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        connection.close()
        return user

    def register_user(self, data):

        if self.get_user(data['username']) is None:
            
            connection = self.db_connection()
            hashed_password  = generate_password_hash(data['password'], method = 'pbkdf2:sha256')
            public_id = str(uuid.uuid4())
            connection.execute("INSERT INTO users (public_id, username, u_password) VALUES (?, ?, ?)", (public_id, data['username'], hashed_password))
            connection.commit()
            connection.close()
            return jsonify({'message': 'user created'})
        return jsonify({'message': 'user already created!'})

    def login_user(self, auth, key):

        if not auth or not auth.username or not auth.password:
            return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic Realm = "Login Required"'})
        user = self.get_user(auth.username)

        if user == None:
            return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic Realm = "Login Required"'})

        if check_password_hash(user[3], auth.password):
            exp_time = int((datetime.datetime.now() + datetime.timedelta(minutes = 20)).timestamp())
            token = jwt.encode({'public_id': user[1], 'username': user[2],'root': user[4], 'exp': exp_time}, key)
            return jsonify({'token': token}), 200
        
        return make_response('Invalid Password!', 401, {'WWW-Authenticate': 'Basic Realm = "Login Required"'})
    
    def logout_user(self, token, key):
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            jwt.decode(token, key, algorithms=['HS256'])
            if token in self.token_black_list:
                return jsonify({'message': 'Invalid Token!'}), 403

            self.token_black_list.add(token)
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid Token!'}), 403

        return jsonify({'message': 'Successfully logged out'}), 200

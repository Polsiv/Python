import sqlite3
import uuid
from flask import jsonify, make_response
from DataBase.initialdatabase import DATA_BASE_ROUTE
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

class Users():

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

        hashed_password  = generate_password_hash(data['password'], method = 'pbkdf2:sha256')
        connection = self.db_connection()
        public_id = str(uuid.uuid4())
        connection.execute("INSERT INTO users (public_id, username, u_password) VALUES (?, ?, ?)", (public_id, data['username'], hashed_password))
        
        connection.commit()
        connection.close()
        return jsonify({'message': 'user created'}), 201

    def login_user(self, auth, key):

        if not auth or not auth.username or not auth.password:
            return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic Realm = "Login Required"'})
        
        user = self.get_user(auth.username)

        if user == None:
            return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic Realm = "Login Required"'})
        
        if check_password_hash(user[3], auth.password):
            exp_time = datetime.datetime.now() + datetime.timedelta(minutes = 10)
            exp_time_timestamp = int(exp_time.timestamp())
            token = jwt.encode({'public_id': user[1], 'exp': exp_time_timestamp}, key)
            return jsonify({'token': token})
        
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic Realm = "Login Required"'})
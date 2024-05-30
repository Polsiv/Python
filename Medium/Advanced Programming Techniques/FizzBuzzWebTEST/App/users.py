import sqlite3
import uuid
from flask import jsonify, make_response
from DataBase.initialdatabase import DATA_BASE_ROUTE
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

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

        if self.get_user(data['username']) is None:
            
            connection = self.db_connection()
            hashed_password  = generate_password_hash(data['password'], method = 'pbkdf2:sha256')
            public_id = str(uuid.uuid4())
            connection.execute("INSERT INTO users (public_id, username, u_password) VALUES (?, ?, ?)", (public_id, data['username'], hashed_password))
            connection.commit()
            connection.close()
            return jsonify({'message': 'user created!'}), 201
        return jsonify({'message': 'user already created!'}), 403

    def login_user(self, data):
        user = self.get_user(data["username"])
        if not user: 
            return jsonify({"message": "User not registered"}), 404

        additional_claims = {"root": user[4]}

        access_token = create_access_token(data["username"], additional_claims=additional_claims)
        return jsonify(access_token=access_token)
    
    def logout_user(self, token, key):
        
        pass
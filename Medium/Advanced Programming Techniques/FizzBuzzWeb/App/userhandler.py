import sqlite3
import uuid
from DataBase.initialdatabase import DATA_BASE_ROUTE
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

class UserHandler():

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
            return {'message': 'user created!'}

        return {'message': 'user already created!'}

    def login_user(self, data):
        user = self.get_user(data["username"])
        if not user: 
            return {"message": "User not registered"}
        
        if check_password_hash(user[3], data["password"]):
            access_token = create_access_token(data["username"])
            return {"message": access_token}
        
        return {"message": "Invalid Password"}

    def logout_user(self, jti, access_expires, redis_block_list):
        redis_block_list.set(jti, "", ex = access_expires)
        return {"message": "Session closed"}
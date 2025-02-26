# We introduce an abstraction (Database) that both MySQLDatabase and MongoDB implement. UserService now depends on the abstraction, not the concrete implementation.

#DIP states that:

#    High-level modules should not depend on low-level modules. Both should depend on abstractions.
#    Abstractions should not depend on details. Details should depend on abstractions.

# This helps decouple modules and makes code easier to maintain and test


from abc import ABC, abstractmethod

# Abstraction
class Database(ABC):
    @abstractmethod
    def get_user(self, user_id):
        pass

# Implementations
class MySQLDatabase(Database):
    def get_user(self, user_id):
        return f"User {user_id} from MySQL"

class MongoDB(Database):
    def get_user(self, user_id):
        return f"User {user_id} from MongoDB"

# High-level module depends on abstraction
class UserService:
    def __init__(self, db: Database):  # Inject dependency (GOOD)
        self.db = db
    
    def get_user_info(self, user_id):
        return self.db.get_user(user_id)

# Usage
mysql_service = UserService(MySQLDatabase())
mongo_service = UserService(MongoDB())

print(mysql_service.get_user_info(1))  # Uses MySQL
print(mongo_service.get_user_info(2))  # Uses MongoDB


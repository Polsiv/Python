from werkzeug.security import generate_password_hash


print(generate_password_hash('depip69420', method = 'pbkdf2:sha256'))
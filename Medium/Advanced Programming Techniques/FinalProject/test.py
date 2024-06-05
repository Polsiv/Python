from werkzeug.security import generate_password_hash, check_password_hash

print(generate_password_hash("depip69420", method = 'pbkdf2:sha256'))

print(check_password_hash('pbkdf2:sha256:600000$mZbAjI3qRKcrVoXG$7bc5271fd369851fd66bc9bb11e0669ab8c57f9b4cf15e8eb0bfe2c4c3443755', 'depip69420'))
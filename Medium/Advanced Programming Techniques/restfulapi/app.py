from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '44def0de75c047b78a198d673c390359'

if __name__ == '__main__':
    app.run(debug = True)
"""Flask factory"""
import os
from flaskr.Core.my_app import MyApp
from flask import Flask, render_template

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/sudoku/', methods = ('GET', 'POST'))
    def display_sudokus():
        """main function that runs our app"""
        myapp = MyApp()
        sudokus = myapp.get_data()
        sudoku_tables = []

        for sudoku in sudokus:
            is_valid, errors = myapp.compute_sudoku(sudoku)
            if is_valid:
                sudoku_table = {'sudoku': sudoku.tolist(), 'errors': 'Sudoku puzzle is valid'}
            else:
                sudoku_table = {'sudoku': sudoku.tolist(), 'errors': errors}
            sudoku_tables.append(sudoku_table)

        return render_template('sudokus.html', sudoku_tables=sudoku_tables)

    return app

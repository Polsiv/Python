# app.py

from flask import Flask, jsonify, request
from sudoku_verifier import is_valid_sudoku

app = Flask(__name__)

@app.route('/verify-sudoku', methods=['POST'])
def verify_sudoku():
    data = request.json
    grid = data.get('grid')
    if not grid:
        return jsonify({'error': 'No Sudoku grid provided'}), 400
    
    if is_valid_sudoku(grid):
        return jsonify({'valid': True}), 200
    else:
        return jsonify({'valid': False}), 200

if __name__ == '__main__':
    app.run(debug=True)

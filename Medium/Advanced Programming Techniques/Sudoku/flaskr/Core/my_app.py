"""module that gets the information and computes it from the other modules"""

from flaskr.Core.file_storage import FileStorage
from flaskr.Core.sudokuverifier import SudokuVerifier
import numpy as np

class MyApp:
    def __init__(self) -> None:
        """Constructor"""
        self.storage = FileStorage()
        self.verifier = SudokuVerifier()

    def get_data(self):
        """method for retrieving the data"""
        sudokus = self.storage.read_data() 
        sudoku_arrays = [np.array(sudoku) for sudoku in sudokus]
        return sudoku_arrays

    def compute_sudoku(self, sudoku):
        """method for computing the retrieved data"""
        return self.verifier.compute_result(sudoku)

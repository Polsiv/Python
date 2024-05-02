from flaskr.Core.file_storage import FileStorage
from flaskr.Core.sudokuverifier import SudokuVerifier

class MyApp:
    def __init__(self) -> None:
        self.storage = FileStorage()
        self.verifier = SudokuVerifier()

    def get_data(self):
        return self.storage.read_data()
    
    def compute_sudoku(self, sudoku):
        return self.verifier.compute_result(sudoku)
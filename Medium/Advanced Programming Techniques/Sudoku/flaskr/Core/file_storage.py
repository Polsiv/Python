"""This module provides the data to our aplication"""
from flaskr.interfaces.i_data_storage import IDataStorage #pylint: disable=C0116

class FileStorage(IDataStorage):

    def read_data(self):
        """reads the input from the text file"""
        with open('./flaskr/InputFiles/input.txt', 'r', encoding="utf-8") as file:
            lines = file.readlines()
            num = int(lines[0])
            data = [line.strip() for line in lines[2:] if line.strip()]

            sudokus = []
            for i in range(num):
                sudoku = []
                for j in range(9):
                    row = [int(digit) for digit in data[j + i * 9]]
                    sudoku.append(row)
                sudokus.append(sudoku)
            return sudokus

    def save_data(self, data):
        """for future development"""

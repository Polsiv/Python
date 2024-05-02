from flaskr.Core.file_storage import FileStorage

def test_invalid_sudoku(client):

    sudokus = FileStorage.read_data()
    data = { 'suudoku' :[
        [7, 9, 9, 2, 3, 5, 4, 1, 8],
        [8, 5, 1, 4, 9, 6, 3, 7, 2],
        [4, 3, 2, 1, 7, 8, 9, 5, 6],
        [1, 7, 4, 5, 6, 9, 2, 8, 3],
        [3, 9, 5, 8, 4, 2, 7, 6, 1],
        [6, 2, 8, 7, 1, 3, 5, 4, 9],
        [2, 8, 3, 6, 5, 7, 1, 9, 4],
        [5, 1, 6, 9, 2, 4, 8, 3, 7],
        [9, 4, 7, 3, 8, 1, 6, 2, 5]
        ]
    }   
    response = client.get('/sudoku/', json=sudokus)
    assert response.status_code == 200
    assert b'Invalid Sudoku' in response.data
    assert b'9 repeated in row 1' in response.data
    assert b'9 repeated in column 2' in response.data
   

def test_valid_sudoku(client):
    sudokus = FileStorage.read_data()
    data = { 'suudoku' :  [ 
        [9, 2, 4, 7, 6, 3, 1, 5, 8],
        [8, 7, 3, 4, 1, 5, 9, 2, 6],
        [1, 6, 5, 9, 2, 8, 3, 4, 7],
        [4, 8, 9, 6, 7, 2, 5, 1, 3],
        [7, 5, 2, 8, 3, 1, 6, 9, 4],
        [3, 1, 6, 5, 4, 9, 8, 7, 2],
        [2, 3, 8, 1, 5, 7, 6, 4, 9],
        [6, 9, 1, 2, 8, 4, 7, 3, 5],
        [5, 4, 7, 3, 9, 6, 2, 8, 1]]

    }
    response = client.get('/sudoku/', json = sudokus)
    assert response.status_code == 200
    assert b'valid sudoku' in response.data


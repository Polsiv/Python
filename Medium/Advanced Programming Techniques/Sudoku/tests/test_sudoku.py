"""module for our test"""

def test_invalid_sudoku(client):
    """test if the sudoku is not valid"""
    response = client.get('/sudoku/')
    assert b"Invalid column 7: ['duplicate 6 at indices 5, 7']" in response.data
    assert b"Invalid column 8: ['duplicate 4 at indices 3, 7']" in response.data

def test_valid_sudoku(client):
    """test if the sudoku is valid"""
    response = client.get('/sudoku/')
    assert b"Errors" not in response.data

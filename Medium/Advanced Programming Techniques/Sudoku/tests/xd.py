def verify_rows(sudoku):
    """Verify if all rows in the Sudoku puzzle are valid."""

    errors = []
    for row_index, row in enumerate(sudoku):
        is_valid, error = is_valid_set(row)
        if not is_valid:
            errors.append(f"Invalid row {row_index + 1}: {error}")
    return not errors, errors

def verify_columns(sudoku):
    """Verify if all columns in the Sudoku puzzle are valid."""

    errors = []
    for col_index in range(9):
        column = [sudoku[row][col_index] for row in range(9)]
        is_valid, error = is_valid_set(column)
        if not is_valid:
            errors.append(f"Invalid column {col_index + 1}: {error}")
    return not errors, errors
def verify_quadrants(sudoku):

    """Verify if all quadrants (3x3 subgrids) in the Sudoku puzzle are valid."""
    errors = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            quadrant = [sudoku[row][col] for row in range(i, i+3) for col in range(j, j+3)]
            is_valid, error = is_valid_set(quadrant)
            if not is_valid:
                quadrant_index = 3 * (i // 3) + (j // 3) + 1
                errors.append(f"Invalid quadrant {quadrant_index}, {error}")
    return not errors, errors


def is_valid_set(nums):
    """Helper function to check if a set of numbers is valid (contains no duplicates)."""
    duplicate_indices = {}  # Initialize the dictionary outside the loop
    for index, num in enumerate(nums):
        if num != 0:
            if num in duplicate_indices:
                duplicate_indices[num].append(index)
            else:
                duplicate_indices[num] = [index]

    errors = []
    for num, indices in duplicate_indices.items():
        adjusted_indices = [index + 1 for index in indices]  # Adjust indices to start from 1
        if len(adjusted_indices) > 1:
            errors.append(f"duplicate {num} at indices {', '.join(map(str, adjusted_indices))}")

    return not errors, errors



def is_valid_sudoku(sudoku):
    """Verify if the entire Sudoku puzzle is valid. """
    row_valid, row_errors = verify_rows(sudoku)
    col_valid, col_errors = verify_columns(sudoku)
    quad_valid, quad_errors = verify_quadrants(sudoku)
    
    if row_valid and col_valid and quad_valid:
        return True, "Sudoku puzzle is valid"
    else:
        errors = row_errors + col_errors + quad_errors
        return False, errors

# The provided Sudoku puzzle
sudoku=[[2, 3, 7, 9, 8, 6, 4, 5, 2],
        [9, 2, 5, 3, 4, 7, 1, 6, 8],
        [8, 6, 4, 5, 2, 1, 9, 7, 3],
        [7, 5, 3, 8, 1, 4, 6, 2, 9],
        [6, 1, 2, 7, 3, 9, 8, 4, 5],
        [4, 8, 9, 6, 5, 2, 3, 1, 7],
        [5, 7, 1, 4, 9, 3, 2, 8, 6],
        [2, 9, 8, 1, 6, 5, 7, 3, 4],
        [3, 4, 6, 2, 7, 8, 5, 9, 1]]

# Check the validity of the Sudoku puzzle
validity, errors = is_valid_sudoku(sudoku)
print("Is the Sudoku puzzle valid?", validity)
if not validity:
    print("Errors:")
    for error in errors:
        print(error)

"""module that ensures our sudokus are valid or not."""

from flaskr.interfaces.i_problem_solver import IProblemSolver

class SudokuVerifier(IProblemSolver):
    """returns validity, and errors if found"""
    def compute_result(self, data):
        return self.is_valid_sudoku(data)

    def verify_rows(self, sudoku):
        """Verify if all rows in the Sudoku  are valid."""

        errors = []
        for row_index, row in enumerate(sudoku):
            is_valid, error = self.is_valid_set(row)
            if not is_valid:
                errors.append(f"Invalid row {row_index + 1}: {error}")
        return not errors, errors

    def verify_columns(self, sudoku):
        """Verify if all columns in the Sudoku are valid."""

        errors = []
        for col_index in range(9):
            column = [sudoku[row][col_index] for row in range(9)]
            is_valid, error = self.is_valid_set(column)
            if not is_valid:
                errors.append(f"Invalid column {col_index + 1}: {error}")
        return not errors, errors
    
    def verify_quadrants(self, sudoku):

        """Verify if all quadrants (3x3 subgrids) in the Sudoku are valid."""
        errors = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                quadrant = [sudoku[row][col] for row in range(i, i+3) for col in range(j, j+3)]
                is_valid, error = self.is_valid_set(quadrant)
                if not is_valid:
                    quadrant_index = 3 * (i // 3) + (j // 3) + 1
                    errors.append(f"Invalid quadrant {quadrant_index}, {error}")
        return not errors, errors

    def is_valid_set(self, nums):
        """Helper function to check if a set of numbers is valid (contains no duplicates)."""
        duplicate_indices = {}
        for index, num in enumerate(nums):
            if num != 0:
                if num in duplicate_indices:
                    duplicate_indices[num].append(index)
                else:
                    duplicate_indices[num] = [index]

        errors = []
        for num, indices in duplicate_indices.items():
            adjusted_indices = [index + 1 for index in indices]
            if len(adjusted_indices) > 1:
                errors.append(f"duplicate {num} at indices {', '.join(map(str, adjusted_indices))}")

        return not errors, errors

    def is_valid_sudoku(self, sudoku):
        """Verify if the entire Sudoku puzzle is valid. """
        row_valid, row_errors = self.verify_rows(sudoku)
        col_valid, col_errors = self.verify_columns(sudoku)
        quad_valid, quad_errors = self.verify_quadrants(sudoku)

        if row_valid and col_valid and quad_valid:
            return True, "Sudoku puzzle is valid"
        else:
            errors = row_errors + col_errors + quad_errors
            return False, errors

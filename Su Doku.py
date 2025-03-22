def solve_sudoku(grid):
    """
    Solves a Sudoku grid using backtracking.
    """
    def is_valid(row, col, num):
        # Check if the number is valid in the current row, column, and 3x3 box
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(row, col, num):
                            grid[row][col] = num
                            if backtrack():
                                return True
                            grid[row][col] = 0
                    return False
        return True

    backtrack()
    return grid

def read_sudoku_file(filename):
    puzzles = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 10):
            grid = []
            for j in range(1, 10):
                row = lines[i + j].strip()
                grid.append([int(c) for c in row])
            puzzles.append(grid)
    return puzzles

def get_top_left_number(grid):
    return int(''.join(map(str, grid[0][:3])))

def main():
    filename = 'p096_sudoku.txt'
    puzzles = read_sudoku_file(filename)
    total_sum = 0

    for puzzle in puzzles:
        solved_grid = solve_sudoku(puzzle)
        top_left_number = get_top_left_number(solved_grid)
        total_sum += top_left_number

    print(f"The sum of the 3-digit numbers in the top-left corners is: {total_sum}")

if __name__ == "__main__":
    main()
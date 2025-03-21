import sys


def read_matrix(file_path):
    with open(file_path, 'r') as file:
        matrix = [[int(num) for num in line.split(',')] for line in file]
    return matrix


def minimal_path_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize the DP table
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    dp[0][0] = matrix[0][0]

    # Fill the first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]

    # Fill the first column
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]

    # Fill the rest of the table
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[rows - 1][cols - 1]


# Read the matrix from the file
file_path = '0081_matrix.txt'
matrix = read_matrix(file_path)

result = minimal_path_sum(matrix)

print(f"The minimal path sum is: {result}")
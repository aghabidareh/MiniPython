import sys


def read_matrix(file_path):
    with open(file_path, 'r') as file:
        matrix = [[int(num) for num in line.split(',')] for line in file]
    return matrix


def minimal_path_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize the DP table with the first column
    dp = [[matrix[i][0] for j in range(cols)] for i in range(rows)]

    for j in range(1, cols):
        # Create a temporary column to store the new DP values
        temp = [0] * rows
        for i in range(rows):
            min_sum = dp[i][j - 1]
            if i > 0:
                min_sum = min(min_sum, dp[i - 1][j])
            if i < rows - 1:
                min_sum = min(min_sum, dp[i + 1][j])
            temp[i] = matrix[i][j] + min_sum
        for i in range(rows):
            dp[i][j] = temp[i]

    min_path_sum = min(dp[i][cols - 1] for i in range(rows))
    return min_path_sum


file_path = '0082_matrix.txt'
matrix = read_matrix(file_path)

result = minimal_path_sum(matrix)

print(f"The minimal path sum is: {result}")
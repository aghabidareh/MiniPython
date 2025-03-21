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

    # Fill the DP table column by column
    for j in range(1, cols):
        # Create a temporary column to store the new DP values
        temp = [0] * rows
        for i in range(rows):
            # Start with the value from the left
            min_sum = dp[i][j - 1]
            # Check the cell above
            if i > 0:
                min_sum = min(min_sum, dp[i - 1][j])
            # Check the cell below
            if i < rows - 1:
                min_sum = min(min_sum, dp[i + 1][j])
            # Update the temporary column
            temp[i] = matrix[i][j] + min_sum
        # Update the DP table with the new column
        for i in range(rows):
            dp[i][j] = temp[i]

    # Find the minimal path sum in the rightmost column
    min_path_sum = min(dp[i][cols - 1] for i in range(rows))
    return min_path_sum


# Read the matrix from the file
file_path = '0082_matrix.txt'
matrix = read_matrix(file_path)

result = minimal_path_sum(matrix)

print(f"The minimal path sum is: {result}")
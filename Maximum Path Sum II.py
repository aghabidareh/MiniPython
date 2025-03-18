def read_triangle(file_path):
    with open(file_path, 'r') as file:
        triangle = [[int(num) for num in line.split()] for line in file]
    return triangle

def max_total(triangle):
    # Start from the second last row and move upwards
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]

# Read the triangle from the file
file_path = '0067_triangle.txt'
triangle = read_triangle(file_path)

result = max_total(triangle)

print(f"The maximum total from top to bottom is: {result}")
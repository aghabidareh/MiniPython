import heapq


def read_matrix(file_path):
    with open(file_path, 'r') as file:
        matrix = [[int(num) for num in line.split(',')] for line in file]
    return matrix


def minimal_path_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = matrix[0][0]

    pq = [(matrix[0][0], 0, 0)]

    while pq:
        current_dist, i, j = heapq.heappop(pq)

        if i == rows - 1 and j == cols - 1:
            return current_dist

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols:
                new_dist = current_dist + matrix[ni][nj]
                if new_dist < dist[ni][nj]:
                    dist[ni][nj] = new_dist
                    heapq.heappush(pq, (new_dist, ni, nj))

    return dist[rows - 1][cols - 1]


file_path = '0083_matrix.txt'
matrix = read_matrix(file_path)

result = minimal_path_sum(matrix)

print(f"The minimal path sum is: {result}")

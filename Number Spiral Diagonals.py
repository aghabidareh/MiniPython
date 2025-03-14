def sum_spiral_diagonals(n):
    if n % 2 == 0:
        raise ValueError("n must be odd")

    total = 1
    for k in range(1, (n // 2) + 1):
        top_right = (2 * k + 1) ** 2
        top_left = top_right - 2 * k
        bottom_left = top_right - 4 * k
        bottom_right = top_right - 6 * k

        total += top_right + top_left + bottom_left + bottom_right

    return total


n = 1001
result = sum_spiral_diagonals(n)
print(f"The sum of the numbers on the diagonals in a {n}x{n} spiral is: {result}")

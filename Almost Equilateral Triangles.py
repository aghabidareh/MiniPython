def find_almost_equilateral_triangles(limit):
    x, y = 2, 1
    sum_perimeters = 0

    while True:
        s = (2 * x - 1) // 3
        if 3 * s - 1 > limit:
            break
        if (2 * x - 1) % 3 == 0:
            perimeter = 3 * s - 1
            sum_perimeters += perimeter

        s = (2 * x + 1) // 3
        if 3 * s + 1 > limit:
            break
        if (2 * x + 1) % 3 == 0:
            perimeter = 3 * s + 1
            sum_perimeters += perimeter

        x, y = 2 * x + 3 * y, 2 * y + x

    return sum_perimeters


def main():
    limit = 10 ** 9
    result = find_almost_equilateral_triangles(limit)
    print(f"The sum of the perimeters is: {result}")


if __name__ == "__main__":
    main()

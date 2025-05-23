def count_right_triangles(limit):
    count = 0

    count += limit * limit

    # Right angle at P
    for x1 in range(1, limit + 1):
        for y1 in range(1, limit + 1):
            for x2 in range(0, limit + 1):
                numerator = x1 * x1 + y1 * y1 - x1 * x2
                if numerator % y1 == 0:
                    y2 = numerator // y1
                    if 0 <= y2 <= limit:
                        count += 1

    for x2 in range(1, limit + 1):
        for y2 in range(1, limit + 1):
            for x1 in range(0, limit + 1):
                numerator = x2 * x2 + y2 * y2 - x2 * x1
                if numerator % y2 == 0:
                    y1 = numerator // y2
                    if 0 <= y1 <= limit:
                        count += 1

    return count


def main():
    limit = 50
    result = count_right_triangles(limit)
    print(f"The number of right triangles is: {result}")


if __name__ == "__main__":
    main()

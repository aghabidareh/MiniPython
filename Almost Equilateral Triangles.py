def find_almost_equilateral_triangles(limit):
    """
    Find all almost equilateral triangles with integral side lengths and area,
    and whose perimeters do not exceed the given limit.
    """
    # Initialize variables for Pell's equation x^2 - 3y^2 = 1
    x, y = 2, 1
    sum_perimeters = 0

    while True:
        # Case 1: Third side is s - 1
        s = (2 * x - 1) // 3
        if 3 * s - 1 > limit:
            break
        if (2 * x - 1) % 3 == 0:
            perimeter = 3 * s - 1
            sum_perimeters += perimeter

        # Case 2: Third side is s + 1
        s = (2 * x + 1) // 3
        if 3 * s + 1 > limit:
            break
        if (2 * x + 1) % 3 == 0:
            perimeter = 3 * s + 1
            sum_perimeters += perimeter

        # Generate the next solution to Pell's equation
        x, y = 2 * x + 3 * y, 2 * y + x

    return sum_perimeters

def main():
    limit = 10**9
    result = find_almost_equilateral_triangles(limit)
    print(f"The sum of the perimeters is: {result}")

if __name__ == "__main__":
    main()
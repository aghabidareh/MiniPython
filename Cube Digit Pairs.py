from itertools import combinations


def can_form_all_squares(cube1, cube2):
    # Define all required square numbers
    squares = ['01', '04', '09', '16', '25', '36', '49', '64', '81']

    # Check if all squares can be formed
    for square in squares:
        a, b = square[0], square[1]
        # Check if a is on cube1 and b is on cube2, or vice versa
        # Also, consider 6 and 9 as interchangeable
        if not ((a in cube1 and b in cube2) or (a in cube2 and b in cube1)):
            # Handle the case where 6 and 9 are interchangeable
            if (a == '6' or a == '9') and (b == '6' or b == '9'):
                if not ((('6' in cube1 or '9' in cube1) and ('6' in cube2 or '9' in cube2))):
                    return False
            else:
                return False
    return True


def generate_cubes():
    digits = set(range(10))
    # Generate all combinations of 6 digits for the first cube
    cubes = list(combinations(digits, 6))
    return cubes


def count_valid_arrangements():
    cubes = generate_cubes()
    count = 0
    # Iterate through all pairs of cubes
    for i in range(len(cubes)):
        for j in range(i, len(cubes)):
            cube1 = cubes[i]
            cube2 = cubes[j]
            # Check if the pair can form all squares
            if can_form_all_squares(cube1, cube2):
                count += 1
    return count


# Count the number of valid arrangements
result = count_valid_arrangements()

print(f"The number of distinct arrangements is: {result}")
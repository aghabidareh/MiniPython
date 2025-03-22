from itertools import combinations


def can_form_all_squares(cube1, cube2):
    # Define all required square numbers
    squares = ['01', '04', '09', '16', '25', '36', '49', '64', '81']

    # Check if all squares can be formed
    for square in squares:
        a, b = square[0], square[1]
        if not ((a in cube1 and b in cube2) or (a in cube2 and b in cube1)):
            if (a == '6' or a == '9') and (b == '6' or b == '9'):
                if not ((('6' in cube1 or '9' in cube1) and ('6' in cube2 or '9' in cube2))):
                    return False
            else:
                return False
    return True


def generate_cubes():
    digits = set(range(10))
    cubes = list(combinations(digits, 6))
    return cubes


def count_valid_arrangements():
    cubes = generate_cubes()
    count = 0
    for i in range(len(cubes)):
        for j in range(i, len(cubes)):
            cube1 = cubes[i]
            cube2 = cubes[j]
            if can_form_all_squares(cube1, cube2):
                count += 1
    return count


result = count_valid_arrangements()

print(f"The number of distinct arrangements is: {result}")
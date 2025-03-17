def generate_polygonal_numbers(sides, limit):
    n = 1
    numbers = []
    while True:
        if sides == 3:
            p = n * (n + 1) // 2
        elif sides == 4:
            p = n * n
        elif sides == 5:
            p = n * (3 * n - 1) // 2
        elif sides == 6:
            p = n * (2 * n - 1)
        elif sides == 7:
            p = n * (5 * n - 3) // 2
        elif sides == 8:
            p = n * (3 * n - 2)
        else:
            raise ValueError("Invalid number of sides")

        if p >= 10000:
            break
        if p >= 1000:
            numbers.append(p)
        n += 1
    return numbers


def is_cyclic_set(numbers):
    for i in range(len(numbers)):
        if str(numbers[i])[2:] != str(numbers[(i + 1) % len(numbers)])[:2]:
            return False
    return True


def find_cyclic_set(polygonal_numbers):
    for triangle in polygonal_numbers[0]:
        for square in polygonal_numbers[1]:
            if str(triangle)[2:] == str(square)[:2]:
                for pentagonal in polygonal_numbers[2]:
                    if str(square)[2:] == str(pentagonal)[:2]:
                        for hexagonal in polygonal_numbers[3]:
                            if str(pentagonal)[2:] == str(hexagonal)[:2]:
                                for heptagonal in polygonal_numbers[4]:
                                    if str(hexagonal)[2:] == str(heptagonal)[:2]:
                                        for octagonal in polygonal_numbers[5]:
                                            if str(heptagonal)[2:] == str(octagonal)[:2] and str(octagonal)[2:] == str(
                                                    triangle)[:2]:
                                                return [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]
    return None


polygonal_numbers = [
    generate_polygonal_numbers(3, 10000),
    generate_polygonal_numbers(4, 10000),
    generate_polygonal_numbers(5, 10000),
    generate_polygonal_numbers(6, 10000),
    generate_polygonal_numbers(7, 10000),
    generate_polygonal_numbers(8, 10000)
]

cyclic_set = find_cyclic_set(polygonal_numbers)

if cyclic_set:
    sum_cyclic_set = sum(cyclic_set)
    print(f"The cyclic set of six numbers is: {cyclic_set}")
    print(f"The sum of the numbers is: {sum_cyclic_set}")
else:
    print("No cyclic set of six numbers found.")

from itertools import permutations
from collections import defaultdict

def is_cube(n, cubes_set):
    # Check if n is a cube
    return n in cubes_set

def find_smallest_cube_with_five_permutations():
    cubes = {}
    cubes_set = set()
    n = 1
    while True:
        cube = n ** 3
        cubes[n] = cube
        cubes_set.add(cube)
        # Check permutations for the current cube
        cube_str = str(cube)
        cube_digits = sorted(cube_str)
        count = 0
        for perm in set([''.join(p) for p in permutations(cube_str)]):
            if perm[0] != '0':
                perm_num = int(perm)
                if perm_num in cubes_set:
                    count += 1
        if count == 5:
            return cube
        n += 1

# Find the smallest cube with exactly five permutations that are also cubes
result = find_smallest_cube_with_five_permutations()

print(f"The smallest cube with exactly five permutations that are also cubes is: {result}")
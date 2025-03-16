def are_permutations(x, multiples):
    x_str = sorted(str(x))
    for multiple in multiples:
        if sorted(str(multiple)) != x_str:
            return False
    return True

def find_smallest_x():
    x = 1
    while True:
        multiples = [2 * x, 3 * x, 4 * x, 5 * x, 6 * x]
        if are_permutations(x, multiples):
            return x
        x += 1

result = find_smallest_x()

print(f"The smallest positive integer x is: {result}")
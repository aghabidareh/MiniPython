#find for pythagorean triplet

def find_pythagorean_triplet(target_sum):
    for a in range(1, target_sum // 3):
        for b in range(a + 1, (target_sum - a) // 2):
            c = target_sum - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a, b, c
    return None

target_sum = 1000

triplet = find_pythagorean_triplet(target_sum)

if triplet:
    a, b, c = triplet
    product = a * b * c
    print(f"The Pythagorean triplet is: ({a}, {b}, {c})")
    print(f"The product abc is: {product}")
else:
    print("No such triplet exists.")
import math

def count_integer_paths(M):
    count = 0
    for a in range(1, M + 1):
        for b in range(a, M + 1):
            # Calculate the minimum c such that a^2 + (b + c)^2 is a perfect square
            # We need to find c such that a^2 + (b + c)^2 = k^2 for some integer k
            # Rearranged: (b + c)^2 = k^2 - a^2
            # So (b + c) must be greater than or equal to b, and less than or equal to M + b
            # We can iterate over possible k values
            min_k = math.ceil(math.sqrt(a**2 + (b + a)**2))
            max_k = math.floor(math.sqrt(a**2 + (b + M)**2))
            for k in range(min_k, max_k + 1):
                c_squared = k**2 - a**2
                if c_squared < (b)**2:
                    continue
                c_plus_b = math.isqrt(c_squared)
                if c_plus_b**2 != c_squared:
                    continue
                c = c_plus_b - b
                if c < b:
                    continue
                if c > M:
                    continue
                count += 1
    return count

def find_min_M(target):
    M = 1
    while True:
        count = count_integer_paths(M)
        if count > target:
            return M
        M += 1

target = 1000000
result = find_min_M(target)

print(f"The least value of M such that the number of solutions first exceeds one million is: {result}")
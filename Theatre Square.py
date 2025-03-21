import math

# Read input values
n, m, a = map(int, input().split())

# Calculate the number of flagstones needed
flagstones_n = math.ceil(n / a)
flagstones_m = math.ceil(m / a)

total_flagstones = flagstones_n * flagstones_m

print(total_flagstones)
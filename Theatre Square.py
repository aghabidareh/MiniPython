import math

n, m, a = map(int, input().split())

flagstones_n = math.ceil(n / a)
flagstones_m = math.ceil(m / a)

total_flagstones = flagstones_n * flagstones_m

print(total_flagstones)
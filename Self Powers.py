def last_ten_digits():
    mod = 10 ** 10
    total = 0
    for n in range(1, 1001):
        total = (total + pow(n, n, mod)) % mod
    return total


result = last_ten_digits()

print(f"The last ten digits of the series are: {result:010d}")

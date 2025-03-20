def count_partitions(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    return dp[n] - 1


n = 100
result = count_partitions(n)

print(f"The number of ways to write 100 as a sum of at least two positive integers is: {result}")

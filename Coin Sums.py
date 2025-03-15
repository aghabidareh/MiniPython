def count_ways_to_make_amount(coins, amount):
    dp = [0] * (amount + 1)

    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


coins = [1, 2, 5, 10, 20, 50, 100, 200]

amount = 200

ways = count_ways_to_make_amount(coins, amount)

print(f"Number of ways to make £2: {ways}")
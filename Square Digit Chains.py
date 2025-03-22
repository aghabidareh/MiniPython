def sum_of_squares(n):
    """
    Calculate the sum of the squares of the digits of n.
    """
    return sum(int(digit) ** 2 for digit in str(n))

def count_numbers_arriving_at_89(limit):
    """
    Count how many numbers below the limit arrive at 89 when repeatedly summing the squares of their digits.
    """
    # Memoization to store whether a number arrives at 89
    memo = {}

    def arrives_at_89(n):
        if n == 1:
            return False
        if n == 89:
            return True
        if n in memo:
            return memo[n]
        # Recursively check the next number in the chain
        result = arrives_at_89(sum_of_squares(n))
        memo[n] = result
        return result

    count = 0
    for i in range(1, limit):
        if arrives_at_89(i):
            count += 1
    return count

def main():
    limit = 10**7
    result = count_numbers_arriving_at_89(limit)
    print(f"The number of starting numbers below {limit} that arrive at 89 is: {result}")

if __name__ == "__main__":
    main()
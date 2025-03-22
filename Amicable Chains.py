def sum_of_proper_divisors(n):
    if n < 2:
        return 0
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            if i == n // i:
                total += i
            else:
                total += i + n // i
        i += 1
    return total


def find_longest_amicable_chain(limit):
    sum_divisors = [0] * (limit + 1)
    for i in range(1, limit + 1):
        sum_divisors[i] = sum_of_proper_divisors(i)

    longest_chain_length = 0
    smallest_member = 0

    visited = [False] * (limit + 1)

    for i in range(1, limit + 1):
        if not visited[i]:
            chain = []
            current = i
            while True:
                if current > limit or visited[current]:
                    break
                visited[current] = True
                chain.append(current)
                current = sum_divisors[current]
                if current in chain:
                    loop_start = chain.index(current)
                    chain_length = len(chain) - loop_start
                    if chain_length > longest_chain_length:
                        longest_chain_length = chain_length
                        smallest_member = min(chain[loop_start:])
                    break

    return smallest_member


def main():
    limit = 1000000
    result = find_longest_amicable_chain(limit)
    print(f"The smallest member of the longest amicable chain is: {result}")


if __name__ == "__main__":
    main()

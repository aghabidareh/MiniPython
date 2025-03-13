def find_first_fibonacci_with_1000_digits():
    a, b = 1, 1
    index = 2

    while True:
        a, b = b, a + b
        index += 1

        if len(str(b)) >= 1000:
            return index


result = find_first_fibonacci_with_1000_digits()
print(result)

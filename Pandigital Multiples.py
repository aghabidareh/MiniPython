def is_pandigital(s):
    return len(s) == 9 and set(s) == set("123456789")


def find_largest_pandigital():
    largest_pandigital = 0

    for i in range(1, 10000):
        concatenated_product = ""
        n = 1
        while len(concatenated_product) < 9:
            concatenated_product += str(i * n)
            n += 1

        if len(concatenated_product) == 9 and is_pandigital(concatenated_product):
            pandigital_number = int(concatenated_product)
            if pandigital_number > largest_pandigital:
                largest_pandigital = pandigital_number

    return largest_pandigital


result = find_largest_pandigital()

print(f"The largest 1 to 9 pandigital 9-digit number is: {result}")

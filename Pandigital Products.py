def is_pandigital(s):
    return len(s) == 9 and set(s) == set("123456789")

def find_pandigital_products():
    products = set()

    for a in range(1, 10):
        for b in range(1000, 10000):
            product = a * b
            combined = f"{a}{b}{product}"
            if len(combined) == 9 and is_pandigital(combined):
                products.add(product)

    for a in range(10, 100):
        for b in range(100, 1000):
            product = a * b
            combined = f"{a}{b}{product}"
            if len(combined) == 9 and is_pandigital(combined):
                products.add(product)

    return sum(products)

result = find_pandigital_products()
print(f"Sum of all unique pandigital products: {result}")
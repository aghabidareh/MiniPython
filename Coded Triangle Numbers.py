import requests

def load_words():
    # Load the words from the file
    url = "https://projecteuler.net/resources/documents/0042_words.txt"
    response = requests.get(url)
    words = response.text.replace('"', '').split(',')
    return words

def calculate_word_value(word):
    return sum(ord(char) - ord('A') + 1 for char in word)

def generate_triangle_numbers(limit):
    triangle_numbers = set()
    n = 1
    while True:
        t_n = n * (n + 1) // 2
        if t_n > limit:
            break
        triangle_numbers.add(t_n)
        n += 1
    return triangle_numbers

def count_triangle_words(words):
    max_length = max(len(word) for word in words)
    max_word_value = 26 * max_length

    triangle_numbers = generate_triangle_numbers(max_word_value)

    count = 0
    for word in words:
        word_value = calculate_word_value(word)
        if word_value in triangle_numbers:
            count += 1
    return count

words = load_words()

result = count_triangle_words(words)

print(f"The number of triangle words is: {result}")
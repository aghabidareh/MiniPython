
import math

def read_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().replace('"', '').split(',')
    return words

def find_anagrams(words):
    anagram_groups = {}
    for word in words:
        key = ''.join(sorted(word))
        if key in anagram_groups:
            anagram_groups[key].append(word)
        else:
            anagram_groups[key] = [word]
    anagram_pairs = [group for group in anagram_groups.values() if len(group) > 1]
    return anagram_pairs

def generate_squares(length):
    min_num = 10 ** (length - 1)
    max_num = 10 ** length
    squares = []
    n = math.isqrt(min_num)
    while True:
        square = n * n
        if square >= max_num:
            break
        squares.append(str(square))
        n += 1
    return squares

def is_valid_mapping(word, square, letter_to_digit):
    if len(word) != len(square):
        return False
    for i in range(len(word)):
        if word[i] in letter_to_digit:
            if letter_to_digit[word[i]] != square[i]:
                return False
        else:
            if square[i] in letter_to_digit.values():
                return False
            letter_to_digit[word[i]] = square[i]
    return True

def find_largest_square(anagram_pairs):
    largest_square = 0
    for pair in anagram_pairs:
        word1, word2 = pair[0], pair[1]
        length = len(word1)
        squares = generate_squares(length)
        for square in squares:
            letter_to_digit = {}
            if is_valid_mapping(word1, square, letter_to_digit):
                square2 = ''
                for letter in word2:
                    square2 += letter_to_digit[letter]
                if square2 in squares:
                    square_num = int(square)
                    if square_num > largest_square:
                        largest_square = square_num
    return largest_square

file_path = '0098_words.txt'
words = read_words(file_path)

anagram_pairs = find_anagrams(words)

result = find_largest_square(anagram_pairs)

print(f"The largest square number formed by any member of a square anagram word pair is: {result}")
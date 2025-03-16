import itertools

def read_encrypted_codes(file_path):
    with open(file_path, 'r') as file:
        encrypted_codes = list(map(int, file.read().strip().split(',')))
    return encrypted_codes

def decrypt_message(encrypted_codes, key):
    decrypted_codes = []
    key_length = len(key)
    for i, code in enumerate(encrypted_codes):
        decrypted_code = code ^ key[i % key_length]
        decrypted_codes.append(decrypted_code)
    return decrypted_codes

def is_valid_plaintext(decrypted_codes):
    decrypted_text = ''.join(map(chr, decrypted_codes))
    common_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I']
    for word in common_words:
        if word in decrypted_text:
            return True
    return False

def find_key_and_decrypt(encrypted_codes):
    for key in itertools.product(range(97, 123), repeat=3):
        decrypted_codes = decrypt_message(encrypted_codes, key)
        if is_valid_plaintext(decrypted_codes):
            return key, decrypted_codes
    return None, None

def calculate_ascii_sum(decrypted_codes):
    return sum(decrypted_codes)

# Read the encrypted codes from the file
file_path = '0059_cipher.txt'
encrypted_codes = read_encrypted_codes(file_path)

# Find the key and decrypt the message
key, decrypted_codes = find_key_and_decrypt(encrypted_codes)

if key:
    ascii_sum = calculate_ascii_sum(decrypted_codes)
    print(f"The key is: {''.join(map(chr, key))}")
    print(f"The decrypted message is: {''.join(map(chr, decrypted_codes))}")
    print(f"The sum of the ASCII values in the original text is: {ascii_sum}")
else:
    print("No valid key found.")
import helpers.lib as lib
def encrypt(plaintext, key):
    ciphertext = ""
    actual_key = generate_vigenere_key(plaintext,key)
    for i in range(len(plaintext)):
        ciphertext += lib.decimal_to_alphabet((lib.alphabet_to_decimal(plaintext[i]) + lib.alphabet_to_decimal(actual_key[i])) % 26)
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    actual_key = generate_vigenere_key(ciphertext,key)
    for i in range(len(ciphertext)):
        plaintext += lib.decimal_to_alphabet((lib.alphabet_to_decimal(ciphertext[i]) - lib.alphabet_to_decimal(actual_key[i])) % 26)
    return plaintext

def generate_vigenere_key(plaintext,key):
    length = len(plaintext)
    result = ""
    for i in range(length):
        result += key[(i % len(key))]
    return result

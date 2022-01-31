import helpers.lib as lib
def encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += lib.decimal_to_alphabet((lib.alphabet_to_decimal(plaintext[i]) + lib.alphabet_to_decimal(key[i% len(key)])) % 26)
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += lib.decimal_to_alphabet((lib.alphabet_to_decimal(ciphertext[i]) - lib.alphabet_to_decimal(key[i% len(key)])) % 26)
    return plaintext


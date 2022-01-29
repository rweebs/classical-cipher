import ciphers.vigenere_standard as vigenere_standard
import helpers.lib as lib

plaintext = "123 Hello World"
print(plaintext)
test = vigenere_standard.encrypt(lib.remove_non_alphabet(plaintext).upper(), "key")
print(test)
print(lib.add_space_every_n_chars(vigenere_standard.decrypt(test,"key"), 5))
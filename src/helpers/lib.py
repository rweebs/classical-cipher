def ascii_to_decimal(char):
    return ord(char)

def decimal_to_ascii(decimal):
    return chr(decimal)

def alphabet_to_decimal(char):
    return ord(char) - ord("A")

def decimal_to_alphabet(decimal):
    return chr(decimal + ord("A"))

def remove_spaces(string):
    return string.replace(" ", "")

def add_space_every_n_chars(string, n):
    return " ".join([string[i:i+n] for i in range(0, len(string), n)])

def remove_non_alphabet(string):
    return "".join([char for char in string if char.isalpha()])

def string_to_ascii_array(string):
    return [ord(x) for x in string]

def ascii_to_string(ascii):
    result=""
    for x in ascii:
        result+=chr(x)
    return result

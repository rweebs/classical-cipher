import io

def encrypt(input_bytes, key):
    result = ""
    for i in range(len(input_bytes)):
        result += key[(i % len(key))]
    output_bytes = bytearray()
    for i in range(len(input_bytes)):
      output_bytes.append(((input_bytes[i]) + ord(key[i % len(key)])) % 256)
    return output_bytes

def decrypt(input_bytes, key):
    output_bytes = bytearray()
    result = ""
    for i in range(len(input_bytes)):
        result += key[(i % len(key))]
    for i in range(len(input_bytes)):
      output_bytes.append(((input_bytes[i]) - ord(key[i % len(key)])) % 256)
    return output_bytes
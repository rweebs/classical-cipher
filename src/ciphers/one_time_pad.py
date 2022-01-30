import sqlite3
import string
import ciphers.vigenere_standard as vigenere_standard
import random

def encrypt(message):
    conn = sqlite3.connect('otp.db')
    key_generated=False
    fixed_key=""
    while not(key_generated):
        key = ''.join(random.choice(string.ascii_uppercase) for _ in range(len(message)))
        cursor = conn.execute(f"SELECT * from keys where key='{key}'")
        if cursor.rowcount == -1:
            fixed_key=key
            key_generated=True
    conn.execute(f"insert into keys (key) values ('{fixed_key}')")
    conn.commit()
    conn.close()
    return (vigenere_standard.encrypt(message,fixed_key),fixed_key)

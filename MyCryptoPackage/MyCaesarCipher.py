__mydoc__ = """
MyCaesarCipher.py
Copyright Nanyang Polytechnic, School of Information Technology

Challenges:
----------
C1. Implement encrypt() and decrypt() to handle only upper case, 

C2. Enhance encrypt() and decrypt() to handle both upper and lower cases, 

C3. Enhance encrypt() and decrypt() to handle all base64 characters, 

"""

# Change: According to C1, C2, C3
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def encrypt(key, plaintext_utf8):
    ciphertext_utf8 = ""

    for character in plaintext_utf8:
        if character in LETTERS:
            # Change: get the character position
            position = LETTERS.find(character)
            position = position + key

            # Change: wrap-around if position >= length of LETTERS
            if position >= len(LETTERS):
                position = position - len(LETTERS)

            # Change: append encrypted character
            ciphertext_utf8 = ciphertext_utf8 + LETTERS[position]

        else:
            # Change: append character without encrypting
            ciphertext_utf8 = ciphertext_utf8 + character

    return ciphertext_utf8


def decrypt(key, ciphertext_utf8):
    decryptedtext_utf = ""

    for character in ciphertext_utf8:
        if character in LETTERS:
            # Change: get the character position
            position = LETTERS.find(character)
            position = position - key

            # Change: wrap-around if position >= length of LETTERS
            if position < 0:
                position = position + len(LETTERS)

            # Change: append encrypted character
            decryptedtext_utf = decryptedtext_utf + LETTERS[position]

        else:
            # Change: append character without encrypting
            decryptedtext_utf = decryptedtext_utf + character

    return decryptedtext_utf

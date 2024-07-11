__mydoc__ = """
MyCaesarCipher_Test.py
Copyright Nanyang Polytechnic, School of Information Technology
"""

from MyCryptoPackage import MyCaesarCipher


def run_test():
    print(__mydoc__)

    # Caesar key, 3 denotes shifting 3 character positions
    key = 3

    plaintext = input("Enter plaintext: ")
    ciphertext = MyCaesarCipher.encrypt(key, plaintext)
    decryptedtext = MyCaesarCipher.decrypt(key, ciphertext)
    print("ciphertext: " + ciphertext)
    print("decryptedtext: " + decryptedtext + "\n")

    return


if __name__ == "__main__":
    run_test()

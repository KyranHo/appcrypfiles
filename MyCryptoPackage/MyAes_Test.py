__mydoc__ = """
MyAes_Test.py
Copyright Nanyang Polytechnic, School of Information Technology
"""

from MyCryptoPackage import MyAes
import base64

def run_test():
    print(__mydoc__)

    plaintext = "Testing AES encrypt and decrypt."
    print("Plaintext : ", plaintext)

    # Gen 256bit AES Key
    keyBase64 = MyAes.genKey(32)
    print("Random 256 bits key in Base64 : ", keyBase64)

    # Encrypt plaintext
    ivBase64, ciphertextBase64 =  MyAes.encrypt(keyBase64, plaintext)
    print("\nEncrypt plaintext")
    print("iv in Base64 : ", ivBase64)
    print("Ciphertext in Base64 : ", ciphertextBase64)

    ivByte = base64.standard_b64decode(ivBase64);
    ciphertextByte = base64.standard_b64decode(ciphertextBase64);
    print("\niv in Bytes : ", ivByte)
    print("Ciphertext in Bytes : ", ciphertextByte)

    ivInt = list(ivByte)
    ciphertextInt = list(ciphertextByte)
    print("\niv in integer : ", ivInt)
    print("ciphertext in integer : ", ciphertextInt)


    # Decrypt ciphertext
    print("\nDecrypting ciphertext")
    decryptedtext = MyAes.decrypt(ciphertextBase64,keyBase64,ivBase64)
    print("decryptedtext : ", decryptedtext)

    fileName = "ciphertext.bin"
    print("\nEncrypt to file")
    print("Filename : ", fileName)
    MyAes.encryptToFile(keyBase64, plaintext, fileName)
    print("Decrypt from file")
    decryptedtextFromFile = MyAes.decryptFromFile(keyBase64, fileName)
    print("decryptedtextFromFile : ", decryptedtextFromFile)

    return


if __name__ == "__main__":
    run_test()

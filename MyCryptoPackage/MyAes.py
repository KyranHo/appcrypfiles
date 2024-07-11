__mydoc__ = """
MyAes.py
Copyright Nanyang Polytechnic, School of Information Technology

Challenges:
----------
C1. Implement genKey(keySize) to return Base64 of random size = keySize x 8 bits.

C2. Implement AES encrypt(keyBase64, plaintext) where:
- keyBase64: AES key in Base64 format
- plaintext_utf8: plaintext in UTF8 format
- assumption: use CBC mode, IV and default padding (PKCS7)
- return: iv and cipherText in Base64 format

C3. Implement AES decrypt(ivBase64, keyBase64, ciphertextBase64) where:
- ivBase64: iv in Base64 format
- keyBase64: AES key in Base64 format
- ciphertextBase64: ciphertext in Base64 format
- assumption: use CBC mode and default padding (PKCS7)
- return: decryptedtext

C4. Implement AES encryptToFile(keyBase64, plaintext, filename) where:
- keyBase64: AES key in Base64 format
- plaintext_utf8: plaintext in UTF8 format
- create filename
- assumption: use CBC mode, IV and default padding (PKCS7)
- return: nil

C5. Implement AES decryptFromFile(keyBase64, filename) where:
- keyBase64: AES key in Base64 format
- filename is name of file with iv and ciphertext
- assumption: use CBC mode, IV and default padding (PKCS7)
- return: decryptedtext

Check that the ciphertext file (ciphertext.bin) is also created.

Optional:
---------
Modify to support CFB and OFB modes.

"""


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64


def genKey(keySize):
    # Change C1: Generate random key of size keySize
    keyBytes = get_random_bytes(keySize)
    # Change C1: Convert key from bytes to base64
    keyBase64 = base64.b64encode(keyBytes)
    return keyBase64

# AES encrypt using CBC and IV, with default padding (PKCS7)

def encrypt(keyBase64, plaintext):
    # convert key and plaintext to bytes
    keyBytes = base64.b64decode(keyBase64)
    plaintextBytes = bytes(plaintext, 'utf-8')
    # Change C2: create cypher with key and CBC mode
    cipher = AES.new(keyBytes, AES.MODE_CBC) #iv is here
    # Change C2: create cyphertext in Bytes
    ciphertextBytes = cipher.encrypt(pad(plaintextBytes, AES.block_size))
    # Change C2: capture iv in Bytes
    ivBytes = cipher.iv
    # Change C2: Convert ciphertext and iv from bytes to base64
    ciphertextBase64 = base64.b64encode(ciphertextBytes)
    ivBase64 = base64.b64encode((ivBytes))

    return ivBase64, ciphertextBase64

def decrypt(ciphertextBase64, keyBase64, ivBase64):
    # Change C3: convert key, iv, ciphertext to bytes
    keyBytes = base64.b64decode(keyBase64)
    ivBytes = base64.b64decode(ivBase64)
    ciphertextBytes = base64.b64decode(ciphertextBase64)
    # Change C3: create cypher with key, iv and specify mode
    cipher = AES.new(keyBytes, AES.MODE_CBC, ivBytes)
    # Change C3: decrypt ciphertext in decryptedtextBytes
    decryptedtextBytes = unpad(cipher.decrypt(ciphertextBytes), AES.block_size)
    # Change C3: convert decryptedtext from bytes to ASCII characters
    decryptedtext = decryptedtextBytes.decode('utf-8')
    return decryptedtext


def encryptToFile(keyBase64, plaintext, fileName):
    # Change C4: convert key and plaintext to bytes
    keyBytes = base64.b64decode(keyBase64)
    plaintextBytes = bytes(plaintext, 'utf-8')
    # Change C4: create cypher with key and specify mode
    cipher = AES.new(keyBytes, AES.MODE_CBC)
    # Change C4: create cyphertext and capture IV in bytes
    ciphertextBytes = cipher.encrypt(pad(plaintextBytes, AES.block_size))
    ivBytes = cipher.iv
    # Change C4: write iv and ciphertext bytes to file
    with open(fileName, "wb") as file_out:
        file_out.write(ivBytes)
        file_out.write(ciphertextBytes)
        file_out.close()
    return


# AES decrypt using CBC and IV, with default unpadding (PKCS7)
def decryptFromFile(keyBase64, fileName):
    # Change C5: convert key and plaintext to bytes
    keyBytes = base64.b64decode(keyBase64)
    # Change C5: read iv and ciphertext bytes from file
    with open(fileName, "rb") as fileIn:
        ivBytes = fileIn.read(AES.block_size)
        ciphertextBytes = fileIn.read()
        fileIn.close()    # Change C5: create cypher with key, iv and specify mode
    cipher = AES.new(keyBytes, AES.MODE_CBC, ivBytes)
    decryptedtextBytes = unpad(cipher.decrypt(ciphertextBytes), AES.block_size)
    decryptedtext = decryptedtextBytes.decode('utf-8')
    return decryptedtext

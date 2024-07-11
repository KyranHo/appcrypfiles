__mydoc__ = """
MyRsa.py
Copyright Nanyang Polytechnic, School of Information Technology

Challenges:

C1. Implement generate_keypair(keySize) to return keyPair of keySize bits

C2. Implement get_private_key(keypair) to extract private key from keyPair

C3. Implement get_public_key(keypair) to extract public key from keyPair

C4. Implement write_private_key(keypair, private_keyfile) 

C5. Implement write_public_key(keypair, public_keyfile)

C6. Implement read_private_key(private_keyfile)

C7. Implement read_public_key(public_keyfile)

C8. Implement encrypt(public_key, plaintext_utf8)

C9. Implement decrypt(private_key, ciphertext_utf8)

----------
"""


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_keypair(keySize):
    # Change C1: Generate keypair
    keyPair = RSA.generate(keySize)
    return keyPair


def get_private_key(keypair):
    # Change C2: Get Private Key from kepair
    privatekey = keypair.export_key()
    privatekeyObj = RSA.import_key(privatekey)
    return privatekeyObj


def get_public_key(keypair):
    # Change C3: Get Public Key from kepair
    publickey = keypair.publickey().export_key()
    publickeyObj = RSA.import_key(publickey)
    return publickeyObj


def write_private_key(keypair, privatekeyFile):
    # Change C4: extract private key
    privatekey = keypair.export_key()
    privateFile = open(privatekeyFile, "wb")
    privateFile.write(privatekey)
    privateFile.close()
    return


def write_public_key(keypair, publickeyFile):
    # Change C5: extract public key
    publickey = keypair.publickey().export_key()
    publicFile = open(publickeyFile, "wb")
    publicFile.write(publickey)
    publicFile.close()
    return

def read_private_key(privatekeyFile):
    # Change C6: extract private key from File
    privatekeyObj = RSA.import_key(open(privatekeyFile,'r').read())
    return privatekeyObj

def read_public_key(publickeyFile):
    # Change C7: extract public key from File
    publickeyObj = RSA.import_key(open(publickeyFile, 'r').read())
    return publickeyObj


    
def encrypt(publickey, plaintext):
    # Change C8: create RSA with public key
    rsa = PKCS1_OAEP.new(publickey)
    ciphertextBytes = rsa.encrypt(plaintext)
    ciphertextBase64 = base64.b64encode(ciphertextBytes).decode('utf-8')
    return ciphertextBase64

def decrypt(privatekey, ciphertextBase64):
    # Change C9: create RSA with private key
    rsa = PKCS1_OAEP.new(privatekey)
    ciphertextBytes = base64.standard_b64decode(ciphertextBase64)
    decryptedtext = rsa.decrypt(ciphertextBytes)
    return decryptedtext


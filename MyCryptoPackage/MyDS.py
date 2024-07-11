__mydoc__ = """
MyDS.py
Copyright Nanyang Polytechnic, School of Information Technology

Challenge:

C1. Implement hash_file_SHA256 to obtain hash of a file
C2. Implement my_sign(privatekey, filename) to sign hasmessage digest hmac
C3. Implement my_verify(publickey, filename, signature) to verify signature using public key

"""



from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15



def hash_file_SHA256(filename):
    # Change C1: create hash
    sha256 = SHA256.new()
    # Change C1: Read content from file and add to hash
    with open(filename, "rb") as input_file:
        while True:
             data = input_file.read()
             if not data:
                 break
             sha256.update(data)
    return sha256

def my_sign(privatekey, filename):
    # Change C2: create hash from file
    hash = hash_file_SHA256(filename)
    # Change C2: sign hash with private key
    signature = pkcs1_15.new(privatekey).sign(hash)
    return signature

def my_verify(publickey, filename, signature):
    # Change C3: create hash from file
    hash = hash_file_SHA256(filename)
    # Change C3: verify signature using publick Key
    try:
        pkcs1_15.new(publickey).verify(hash, signature)
        return "Verified from sender"
    except (ValueError, TypeError):
        return "Integrity or Authentication error"

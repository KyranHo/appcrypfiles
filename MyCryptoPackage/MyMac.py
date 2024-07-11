__mydoc__ = """
MyMac.py
Copyright Nanyang Polytechnic, School of Information Technology

Challenge:

C1. Implement gen_key() to generate random 256 bits
C2. Implement get_hmac(key, plaintext_utf8) to message digest hmac
C3. Implement verify_hmac(key, plaintext_utf8, hmacMd) to compare hmacMd with hmac generated using key and plaintext_utf8

"""


from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes


def gen_key():
    # Change C1: Generate random key of 256 bits
    keyBytes = get_random_bytes(32)
    return keyBytes



def get_hmac(key, plaintext_utf8):
    # Change C2: Generate HMAC
    hmac = HMAC.new(key, digestmod=SHA256)
    # Change C2: update hmac with plaintext
    hmac.update(plaintext_utf8)
    # Change C2: generate hexidecimal hmac
    hmacMd = hmac.hexdigest()
    return hmacMd


def verify_hmac(key, plaintext_utf8, hmacMd):
    # Change C3: Generate HMAC
    computed_hmac = HMAC.new(key, digestmod=SHA256)
    # Change C3: update hmac with plaintext
    computed_hmac.update(plaintext_utf8)
    # Change C3: generate hexidecimal hmac
    computed_hmacMd = computed_hmac.hexdigest()
    # Change C3: Compare hmac with computed hmac
    if hmacMd == computed_hmacMd:
       return "Matched"
    else:
       return "Not Matched"

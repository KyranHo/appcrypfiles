__mydoc__ = """
MyBase64Converter.py
Copyright Nanyang Polytechnic, School of Information Technology

Challenges:
----------
C1. Using Crypto.Random

C2. Enhance encrypt() and decrypt() to handle both upper and lower cases, 

C3. Enhance encrypt() and decrypt() to handle all base64 characters, 

"""

import Crypto.Random
from Crypto.Random import get_random_bytes
import base64

def generateRandom(numOfBytes):
    # Change C1: Generate random
    key_bytes = get_random_bytes(numOfBytes)
    return key_bytes

def bytesToBase64(inBytes):
    # Change C2: Convert bytes to base64
    inBase64 = base64.encodebytes(inBytes)
    return inBase64

def base64ToBytes(inBase64):
    # Change C2: Convert base64 to bytes
    inBytes = base64.decodebytes(inBase64)
    return inBytes
__mydoc__="""
MyModule_TestAll.py
Copyright Nanyang Polytechnic, School of Information Technology
"""

from MyCryptoPackage import MyModule_Test
from MyCryptoPackage import MyCaesarCipher_Test
# from MyCryptoPackage import MyAes_Test
# from MyCryptoPackage import MyRsa_Test
# from MyCryptoPackage import MyHash_Test


def run_test():
    print(__mydoc__)

    MyModule_Test.run_test()
    MyCaesarCipher_Test.run_test()
    # MyAes_Test.run_test()
    # MyRsa_Test.run_test()
    # MyHash_Test.run_test()

    return

if __name__ == "__main__":
    run_test()
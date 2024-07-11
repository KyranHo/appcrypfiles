__mydoc__ = """
MyBase64Converter_Test.py
Copyright Nanyang Polytechnic, School of Information Technology
"""

from MyCryptoPackage import MyBase64Converter


def run_test():

    print(__mydoc__)

    print("Generate 8 bytes of Random Bytes")
    testBytes=MyBase64Converter.get_random_bytes(8)
    print("Print :", testBytes)
    print("Convert bytes to base64")
    testBytesBase64 = MyBase64Converter.bytesToBase64(testBytes)
    print("In base64", testBytesBase64)
    print("Convert base64 to bytes")
    testBytes = MyBase64Converter.base64ToBytes(testBytesBase64)
    print("Print :", testBytes)

    return


if __name__ == "__main__":
    run_test()
__mydoc__="""
MyModule_Test.py
Copyright Nanyang Polytechnic, School of Information Technology
"""

from MyCryptoPackage import MyModule


def run_test():
    print(__mydoc__)

    print("MyModule_Test.py: run_test() is called.")
    MyModule.my_method()

    return

if __name__ == "__main__":
    run_test()
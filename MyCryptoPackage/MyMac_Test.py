__mydoc__ = """
----------------------------------------------------------------------------
MyMac_Test.py
Copyright Nanyang Polytechnic, School of Information Technology
"""


from MyCryptoPackage import MyMac


def run_test():
    print(__mydoc__)

    original_string = "Original message"
    altered_string = "0riginal message"

    print("Original Text :" + original_string)

    # Sender creates secret Key
    secretKey = MyMac.gen_key()
    print("\nSender creates secret Key which he shares only with Receiver:")
    print(secretKey)

    # Sender creates hmac
    hmacMd = MyMac.get_hmac(secretKey, original_string.encode("utf8"))
    print("\nSender creates hmac from original text and secret key:")
    print("Sender sends hmac and original text to Receiver.")
    print("  Message : " + original_string)
    print("  MAC     : " + hmacMd)

    # Receiver compares received hmac with hmac he generates from original text and secret key
    verify = MyMac.verify_hmac(secretKey, original_string.encode("utf8"), hmacMd)
    print("\nReceiver compares received hmac with hmac he generates from original text and secret key :")
    print("  " + verify)

    # Attacker alters text
    print("\nAttacker intercepts messages and alters text and sends to Receiver:")
    print(altered_string)

    print("\nAttacker sends original hmac and altered text to Receiver.")
    print("  a_Message : " + altered_string)
    print("  MAC     : " + hmacMd)

    # Receiver compares received hmac with hmac he generates from altered text and secret key
    verify = MyMac.verify_hmac(secretKey, altered_string.encode("utf8"), hmacMd)
    print("\nReceiver compares received hmac with hmac he generates from altered text and secret key")
    print("  " + verify)

    # attacker generates hmac
    a_secretKey = MyMac.gen_key()
    print("\nAttacker secret key :")
    print(a_secretKey)

    a_hmacMd = MyMac.get_hmac(a_secretKey, altered_string.encode("utf8"))
    print("Attacker generates his own hmac from altered text and his own secret key:")
    print(a_hmacMd)

    print("\nAttacker sends altered hmac and altered text to Receiver.")
    print("  a_Message : " + altered_string)
    print("  a_MAC     : " + a_hmacMd)

    # Receiver compares altered hmac with hmac he generates from altered text and secret key
    verify = MyMac.verify_hmac(secretKey, altered_string.encode("utf8"), hmacMd)
    print("\nReceiver compares received hmac with hmac he generates from altered text and secret key")
    print("  " + verify)

    return

if __name__ == "__main__":
    run_test()

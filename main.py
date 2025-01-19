from sha_1 import *
from sha_256 import *
import os


def menu():
    msg = input("Insert the text that you want to hash: ")
    msg_bytes = f'b"{msg}"'.encode()

    rezultat_sha1 = sha1(msg_bytes)
    rezultat_sha256 = sha256(msg_bytes)

    str_1 = hashlib.sha1(msg_bytes)
    str_hex_1 = str_1.hexdigest()

    str_256 = hashlib.sha256(msg_bytes)
    str_hex_256 = str_256.hexdigest()

    print(f"Hash-ul SHA-1 pentru mesajul '{msg}' este: {rezultat_sha1}")
    print(f"Hash-ul SHA-1, folosind libraria hashlib, pentru mesajul '{msg}' este: {str_hex_1}\n")

    print(f"Hash-ul SHA-256 pentru mesajul '{msg}' este: {rezultat_sha256}")
    print(f"Hash-ul SHA-256, folosind libraria hashlib, pentru mesajul '{msg}' este: {str_hex_256}\n")


if __name__ == "__main__":
    menu()

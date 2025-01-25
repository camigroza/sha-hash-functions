from sha_1 import *
from sha_256 import *
from sha_512 import *
import hashlib


def menu():
    msg = input("Insereaza textul: ")
    print()
    msg_bytes = f'b"{msg}"'.encode()

    rezultat_sha1 = sha1(msg_bytes)
    rezultat_sha256 = sha256(msg_bytes)
    rezultat_sha512 = sha512(msg_bytes)

    str_1 = hashlib.sha1(msg_bytes)
    str_hex_1 = str_1.hexdigest()

    str_256 = hashlib.sha256(msg_bytes)
    str_hex_256 = str_256.hexdigest()

    str_512 = hashlib.sha512(msg_bytes)
    str_hex_512 = str_512.hexdigest()

    print(f"Hash-ul SHA-1 este: {rezultat_sha1}")
    print(f"Hash-ul SHA-1, folosind libraria hashlib, este: {str_hex_1}\n")

    print(f"Hash-ul SHA-256 este: {rezultat_sha256}")
    print(f"Hash-ul SHA-256, folosind libraria hashlib, este: {str_hex_256}\n")

    print(f"Hash-ul SHA-512 este: {rezultat_sha512}")
    print(f"Hash-ul SHA-512, folosind libraria hashlib, este: {str_hex_512}\n")


if __name__ == "__main__":
    menu()

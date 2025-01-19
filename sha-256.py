import struct
import binascii
import hashlib


def right_rotate(value, shift):
    """Realizează o rotație circulară la dreapta a valorii pe 32 de biți."""
    return ((value >> shift) | (value << (32 - shift))) & 0xFFFFFFFF


def sha256(message):
    """Implementare a algoritmului SHA-256."""
    # Constantele SHA-256 (primele 32 de biți ai rădăcinilor pătrate ale primelor 64 de numere prime)
    K = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

    # Hash-urile inițiale (primele 32 de biți ai rădăcinilor pătrate ale primelor 8 numere prime)
    H = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    ]

    # Pasul 1: Pre-procesare
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8

    # Adăugăm un bit '1'
    message += b'\x80'

    # Adăugăm padding cu zerouri până la 56 bytes (448 biți mod 512)
    while (len(message) % 64) != 56:
        message += b'\x00'

    # Adăugăm lungimea originală a mesajului, pe 64 de biți
    message += struct.pack('>Q', original_bit_len)

    # Pasul 2: Procesăm mesajul în blocuri de 512 biți (64 bytes)
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]

        # Divizăm chunk-ul în 16 cuvinte de 32 de biți fiecare
        words = list(struct.unpack('>16I', chunk))

        # Extindem lista la 64 de cuvinte
        for j in range(16, 64):
            s0 = right_rotate(words[j - 15], 7) ^ right_rotate(words[j - 15], 18) ^ (words[j - 15] >> 3)
            s1 = right_rotate(words[j - 2], 17) ^ right_rotate(words[j - 2], 19) ^ (words[j - 2] >> 10)
            words.append((words[j - 16] + s0 + words[j - 7] + s1) & 0xFFFFFFFF)

        # Inițializăm variabilele temporare
        a, b, c, d, e, f, g, h = H

        # Main loop: 64 de runde de procesare
        for j in range(64):
            S1 = right_rotate(e, 6) ^ right_rotate(e, 11) ^ right_rotate(e, 25)
            ch = (e & f) ^ ((~e) & g)
            temp1 = (h + S1 + ch + K[j] + words[j]) & 0xFFFFFFFF
            S0 = right_rotate(a, 2) ^ right_rotate(a, 13) ^ right_rotate(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xFFFFFFFF

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF

        # Adăugăm valorile temporare la hash-urile inițiale
        H = [
            (H[0] + a) & 0xFFFFFFFF,
            (H[1] + b) & 0xFFFFFFFF,
            (H[2] + c) & 0xFFFFFFFF,
            (H[3] + d) & 0xFFFFFFFF,
            (H[4] + e) & 0xFFFFFFFF,
            (H[5] + f) & 0xFFFFFFFF,
            (H[6] + g) & 0xFFFFFFFF,
            (H[7] + h) & 0xFFFFFFFF
        ]

    # Pasul 3: Concatenăm rezultatele pentru a obține hash-ul final
    digest = struct.pack('>8I', *H)
    return binascii.hexlify(digest).decode('utf-8')


# Exemplu de utilizare
if __name__ == "__main__":
    mesaj = b"cosmo"
    hash_rezultat = sha256(mesaj)
    print(f"Hash-ul SHA-256 pentru mesajul '{mesaj.decode()}' este: {hash_rezultat}")

    str = hashlib.sha256(b'cosmo')
    str_hex = str.hexdigest()
    print(str_hex)
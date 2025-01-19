import struct
import binascii


def left_rotate(value, shift):
    return ((value << shift) & 0xFFFFFFFF) | (value >> (32 - shift))


def sha1(message):
    # Initializam valorile hash
    H0 = 0x67452301
    H1 = 0xEFCDAB89
    H2 = 0x98BADCFE
    H3 = 0x10325476
    H4 = 0xC3D2E1F0

    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8

    # Adaugam un bit '1'
    message += b'\x80'

    # Adaugam padding cu zerouri pana la 56 bytes
    while (len(message) % 64) != 56:
        message += b'\x00'

    # Adaugam lungimea originala a mesajului, pe 64 de biti
    message += struct.pack('>Q', original_bit_len)

    # Procesam mesajul in blocuri de 512 biti (64 bytes)
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]

        # Divizam chunk-ul in 16 cuvinte de 32 de biti fiecare
        words = list(struct.unpack('>16I', chunk))

        # Extindem lista la 80 de cuvinte
        for j in range(16, 80):
            word = left_rotate(words[j - 3] ^ words[j - 8] ^ words[j - 14] ^ words[j - 16], 1)
            words.append(word)

        # Initializam variabilele temporare
        a, b, c, d, e = H0, H1, H2, H3, H4

        # Main loop: 80 de runde de procesare
        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + words[j]) & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        # Adaugam valorile temporare la hash-urile initiale
        H0 = (H0 + a) & 0xFFFFFFFF
        H1 = (H1 + b) & 0xFFFFFFFF
        H2 = (H2 + c) & 0xFFFFFFFF
        H3 = (H3 + d) & 0xFFFFFFFF
        H4 = (H4 + e) & 0xFFFFFFFF

    # Concatenam rezultatele pentru a obtine hash-ul final
    digest = struct.pack('>5I', H0, H1, H2, H3, H4)
    return binascii.hexlify(digest).decode('utf-8')


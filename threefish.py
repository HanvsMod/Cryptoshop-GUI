import botan
import sys

iterations = 1000000
output_size = 64


def encrypt(filename, passphrase, mode):
    with open(filename, 'rb') as fo:
        input = fo.read()
        fo.close()

    algorithm = "Threefish" + "/" + mode  # AES-128/GCM , Serpent/CTR etc...
    print(algorithm)

    encryptor = botan.cipher(algo=algorithm, encrypt=True)
    rng = botan.rng()

    iv = botan.rng().get(16)

    salt = rng.get(256)

    key = botan.pbkdf(algo="PBKDF2(SHA-256)", password=passphrase, out_len=output_size, iterations=iterations,
                      salt=salt)

    hmackey = botan.hash_function('SHA-512')
    hmackey.update(key[2])
    hmackey.update('MAC')
    h1 = hmackey.final()

    enckey = botan.hash_function('SHA-512')
    enckey.update(key[2])
    enckey.update('encrypt')
    h2 = enckey.final()

    del key

    print(botan.hex_encode(h1))
    print(botan.hex_encode(h2))

    encryptor.set_key(h2)
    encryptor.start(iv)
    cipher = encryptor.finish(input)
    print("vi : " + botan.hex_encode(iv))
    print("salt :" + botan.hex_encode(salt))
    print("cipher : " + botan.hex_encode(cipher))

    hmac = botan.message_authentication_code(algo='HMAC(SHA-256)')
    hmac.set_key(h1)
    hmac.update(cipher)
    hmac.update(salt)
    hmac.update(iv)
    test = hmac.final()

    with open(filename + ".enc", 'wb') as fo:
        fo.write(test)  # hmac 32 bits
        fo.write(iv)  # vi 10 bits
        fo.write(salt)  # salt 16 bits
        fo.write(cipher)  # cipher
        fo.close()
    return "Successfully Encrypted"


def decrypt(filename, m_key):
    with open(filename, 'rb') as fo:
        hmac = fo.read(32)
        iv = fo.read(16)
        salt = fo.read(256)
        cipher = fo.read()
        fo.close()

    decryptor = botan.cipher(mode, encrypt=False)

    key = botan.pbkdf(algo="PBKDF2(SHA-256)", password=m_key, out_len=output_size, iterations=iterations,
                      salt=salt)

    hmackey = botan.hash_function('SHA-256')
    hmackey.update(key[2])
    hmackey.update('MAC')
    h1 = hmackey.final()

    enckey = botan.hash_function('SHA-256')
    enckey.update(key[2])
    enckey.update('encrypt')
    h2 = enckey.final()

    del key

    # hmac verification
    computed_hmac = botan.message_authentication_code(algo='HMAC(SHA-256)')
    computed_hmac.set_key(h1)
    computed_hmac.update(cipher)
    computed_hmac.update(salt)
    computed_hmac.update(iv)
    test = computed_hmac.final()

    print("HMAC Verification : " + str(test == hmac))
    if test == hmac:
        decryptor.set_key(h2)
        decryptor.start(iv)
        decrypted = decryptor.finish(cipher)
        with open(filename + ".decrypted", 'wb') as fo2:
            fo2.write(decrypted)
            fo2.close()
        return "Successfully Decrypted"
    else:
        return "Invalid Hmac verification"

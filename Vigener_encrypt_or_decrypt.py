
def vigenere_encrypt(text, key):
    text = text.upper()
    key = key.upper()

    extended_key = (key * (len(text) // len(key) + 1))[:len(text)]

    ciphertext = []

    for p_char, k_char in zip(text, extended_key):
        if p_char.isalpha():
            encrypted_char = chr(((ord(p_char) - ord('A') + ord(k_char) - ord('A')) % 26) + ord('A'))
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(p_char) 


    return ''.join(ciphertext)


def vigenere_decrypt(text, key):
    text = text.upper()
    key = key.upper()
    extended_key = (key * (len(text) // len(key) + 1))[:len(text)]
    plaintext = []
    for c_char, k_char in zip(text, extended_key):
        if c_char.isalpha():
            decrypted_char = chr(((ord(c_char) - ord('A') - (ord(k_char) - ord('A'))) % 26) + ord('A'))
            plaintext.append(decrypted_char)
        else:
            plaintext.append(c_char) 
    return ''.join(plaintext)
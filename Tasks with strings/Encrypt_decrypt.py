def vigenere_encrypt(message, key):
    encrypt_message = ""
    key_lenght = len(key)
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            key_char = key[i % key_lenght].upper()
            shift = ord(key_char) - ord("A")
            if char.isupper():
                encrypt_message += chr((ord(char) + shift - ord("A")) % 26 + ord("A"))
            else:
                encrypt_message += chr((ord(char) + shift - ord("a")) % 26 + ord("a"))
        else:
            encrypt_message += char
    return encrypt_message


def vigenere_decrypt(encrypted_message, key):
    decrypted_message = ""
    key_lenght = len(key)
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        if char.isalpha():
            key_char = key[i % key_lenght].upper()
            shift = ord(key_char) - ord("A")
            if char.isupper():
                decrypted_message += chr((ord(char) - shift - ord("A")) % 26 + ord("A"))
            else:
                decrypted_message += chr((ord(char) - shift - ord("a")) % 26 + ord("a"))
        else:
            decrypted_message += char
    return decrypted_message


def caesar_encrypt(message, shift):
    encrypt_message = ""
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            if char.isupper():
                encrypt_message += chr((ord(char) + shift - ord("A")) % 26 + ord("A"))
            else:
                encrypt_message += chr((ord(char) + shift - ord("a")) % 26 + ord("a"))
        else:
            encrypt_message += char
    return encrypt_message


def caesar_decrypt(encrypted_message, shift):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        if char.isalpha():
            if char.isupper():
                decrypted_message += chr((ord(char) - shift - ord("A")) % 26 + ord("A"))
            else:
                decrypted_message += chr((ord(char) - shift - ord("a")) % 26 + ord("a"))
        else:
            decrypted_message += char
    return decrypted_message


message_to_encrypt = "HELLO FRIEND"
vigenere_key = "KEY"
caesar_shift = 3

encrypted_vigenere = vigenere_encrypt(message_to_encrypt, vigenere_key)
encrypted_caesar = caesar_encrypt(message_to_encrypt, caesar_shift)

decrypted_vigenere = vigenere_decrypt(encrypted_vigenere, vigenere_key)
decrypted_caesar = caesar_decrypt(encrypted_caesar, caesar_shift)

print("Original Message:", message_to_encrypt)
print("Encrypted Vigenere:", encrypted_vigenere)
print("Encrypted Caesar:", encrypted_caesar)

print("Decrypted Vigenere:", decrypted_vigenere)
print("Decrypted Caesar:", decrypted_caesar)
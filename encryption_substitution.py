def encrypt_ceaser(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_ceasar(ciphertext, shift):
    return encrypt_ceaser(ciphertext, -shift)

plaintext = "Hello, world!"
shift = 3
encrypted = encrypt_ceaser(plaintext, shift)
decrypted = decrypt_ceasar(encrypted, shift)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
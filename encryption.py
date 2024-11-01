import time
import threading

#Encryption and decryption functions
def encrypt_substitution(plaintext, shift=3):
    encrypted = ''.join(chr((ord(char) - 65 + shift) % 26 + 65) if char.isalpha() else char for char in plaintext.upper())
    return encrypted

def decrypt_substitution(ciphertext, shift=3):
    decrypted = ''.join(chr((ord(char) - 65 - shift) % 26 + 65) if char.isalpha() else char for char in ciphertext.upper())
    return decrypted

def encrypt_rail_fence(plaintext, num_rails=3):
    rails = [''] * num_rails
    direction = 1
    row = 0
    for char in plaintext:
        rails[row] += char
        row += direction
        if row == 0 or row == num_rails - 1:
            direction *= -1
            
    return ''.join(rails)

def decrypt_rail_fence(ciphertext, num_rails=3):
    rail_lens = [0] * num_rails
    direction = 1
    row = 0
    for _ in ciphertext:
        rail_lens[row] += 1
        row += direction
        if row == 0 or row == num_rails - 1:
            direction *= -1
    rails, idx = [], 0
    for  length in rail_lens:
        rails.append(ciphertext[idx:idx + length])
        idx += length
    plaintext, row, direction = "", 0, 1
    for _ in ciphertext:
        plaintext += rails[row][0]
        rails[row] = rails[row][1:]
        row += direction
        if row == 0 or row == num_rails - 1:
            direction *= -1
    return plaintext

def encrypt_permutation(plaintext, key=[2, 0, 3, 1]):
    block_size, ciphertext = len(key), ""
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        if len(block) < block_size:
            block += ' ' * (block_size - len(block))
        ciphertext += ''.join(block[k] for k in key if k < len(block))
    return ciphertext

def decrypt_permutation(ciphertext, key=[2,0, 3, 1]):
    block_size, plaintext = len(key), ""
    inverse_key = [key.index(i) for i in range(block_size)]
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        plaintext += ''.join(block[inverse_key[j]] for j in range(block_size)).strip()
    return plaintext

def decrypt_with_timeout(decrypt_func, *args, timeout=2):
    result = [None]
    def wrapper():
        result[0] = decrypt_func(*args)
    
    thread = threading.Thread(target=wrapper)
    thread.start()
    thread.join(timeout)
    
    if thread.is_alive():
        return "Timeout"
    else:
        return result[0]
    
plaintext = input("Enter the text to encrypt: ")

encrypt_substitution = encrypt_substitution(plaintext)
encrypt_rail_fence = encrypt_rail_fence(plaintext)
encrypt_permutation = encrypt_permutation(plaintext)

print("\nEncryption Result:")
print("Substitution Cipher:", encrypt_substitution)
print("Rail Fence Cipher:", encrypt_permutation)
print("Permutation Cipher:", encrypt_permutation)

timeout_duration = 2
print("\nDecryption Results with Timeout:")

decrypt_substitution = decrypt_with_timeout(decrypt_substitution, encrypt_substitution)
print("Substitution Cipher Decryption:", decrypt_substitution)

decrypt_rail_fence = decrypt_with_timeout(decrypt_rail_fence, encrypt_rail_fence)
print("Rail Fence Cipher Decryption:", decrypt_rail_fence)

decrypt_permutation = decrypt_with_timeout(decrypt_permutation, encrypt_permutation)
print("Permutation Cipher Decryption:", decrypt_permutation)        
    
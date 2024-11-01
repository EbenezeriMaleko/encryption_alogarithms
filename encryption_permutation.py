def encrypt_permutation(plaintext, key):
    block_size = len(key)
    ciphertext = ""
  
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        if len(block) < block_size:
            block += ' ' * (block_size - len(block))
                             
        encrypted_block = ''.join(block[k] for k in key if k < len(block))
        ciphertext += encrypted_block

    return ciphertext


def decrypt_permutation(ciphertext, key):
    block_size = len(key)
    plaintext = ""
    
    inverse_key = [key.index(i) for i in range(block_size)]
    
    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        
        decrypted_block = ''.join(block[inverse_key[j]] for j in range(block_size))
        plaintext += decrypted_block.strip()
        
    return plaintext

plaintext = "HELLO_WORLD"
key = [2, 0, 3, 1]
encrypted = encrypt_permutation(plaintext, key)
decrypted = decrypt_permutation(encrypted, key)

print("Plaintext:", plaintext)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
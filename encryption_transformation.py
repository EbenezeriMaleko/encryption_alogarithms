def encrypt_rail_fence(plainttext, num_rails):
    rails = [''] * num_rails
    direction = 1
    row = 0
    
    for char in plainttext:
        rails[row] += char
        row += direction
        
        if row == 0 or row == num_rails -1:
            direction *= -1
            
    return ''.join(rails)

def decrypt_rail_fence(ciphertext, num_rails):
    rail_lens = [0] * num_rails
    direction = 1
    row = 0
    
    for _ in ciphertext:
        rail_lens[row] += 1
        row += direction
        if row == 0 or row == num_rails - 1:
            direction *= -1
            
    rails = []
    idx = 0
    for length in rail_lens:
        rails.append(ciphertext[idx:idx + length])
        idx += length
    
    plaintext = ""
    row = 0
    for length in rail_lens:
        rails.append(ciphertext[idx:idx + length])
        idx += length
        
    plaintext = ""
    row = 0
    direction = 1
    for _ in ciphertext:
        plaintext += rails[row][0]
        rails[row] = rails[row][1:]
        row += direction
        if row == 0 or row == num_rails - 1:
            direction *= -1
            
    return plaintext

plaintext = "HELLO_WORLD"
num_rails = 3
encrpted = encrypt_rail_fence(plaintext, num_rails)
decrypted = decrypt_rail_fence(encrpted, num_rails)

print("Plaintext:", plaintext)
print("Encrypted:", encrpted)
print("Decrypted:", decrypted)
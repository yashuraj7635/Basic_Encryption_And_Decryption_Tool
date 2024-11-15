# Function to encrypt the message
def encrypt_message(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            # Shift character and keep within alphabet bounds
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char  # Non-alphabet characters are not shifted
    return encrypted_message

# Function to decrypt the message
def decrypt_message(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            # Reverse shift character and keep within alphabet bounds
            decrypted_message += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_message += char  # Non-alphabet characters are not shifted
    return decrypted_message

# Main program to demonstrate encryption and decryption
if __name__ == "__main__":
    # Input message
    message = input("Enter a message to encrypt: ")
    shift = int(input("Enter shift value (e.g., 3): "))
    
    # Encrypt the message
    encrypted = encrypt_message(message, shift)
    print(f"Encrypted message: {encrypted}")
    
    # Decrypt the message
    decrypted = decrypt_message(encrypted, shift)
    print(f"Decrypted message: {decrypted}")
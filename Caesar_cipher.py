def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            # Determine ASCII base (97 for lowercase, 65 for uppercase)
            ascii_base = 65 if char.isupper() else 97
            # Convert to 0-25 range, apply shift, and wrap around with modulo
            shifted = (ord(char) - ascii_base + shift) % 26
            # Convert back to character
            encrypted += chr(shifted + ascii_base)
        else:
            # Keep non-alphabetic characters unchanged
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    # Decryption is just encryption with negative shift
    return caesar_encrypt(text, -shift)

def main():
    # Test cases
    message = "Hello, World!"
    shift_value = 3
    
    print(f"Original message: {message}")
    print(f"Shift value: {shift_value}")
    
    # Encryption test
    encrypted = caesar_encrypt(message, shift_value)
    print(">>> caesar_encrypt(\"Hello, World!\", 3)")
    print(f"Encrypted: {encrypted}")
    
    # Decryption test
    decrypted = caesar_decrypt(encrypted, shift_value)
    print(">>> caesar_decrypt(encrypted, 3)")
    print(f"Decrypted: {decrypted}")

if __name__ == "__main__":
    main()
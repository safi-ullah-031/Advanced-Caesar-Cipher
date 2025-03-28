import sys
from caesar_des_encryption import CaesarDESCipherEncrypt
from caesar_des_decryption import CaesarDESCipherDecrypt

def main():
    print("=== Advanced Caesar Cipher ===")
    
    key = input("Enter 8-character key: ").strip()
    shift = int(input("Enter shift value: ").strip())

    while True:
        print("\nOptions:")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            cipher = CaesarDESCipherEncrypt(key, shift)
            text = input("Enter text to encrypt: ")
            result = cipher.encrypt(text)
            print(f"\nEncrypted Text: {result}")

        elif choice == "2":
            cipher = CaesarDESCipherDecrypt(key, shift)
            text = input("Enter text to decrypt: ")
            result = cipher.decrypt(text)
            print(f"\nDecrypted Text: {result}")

        elif choice == "3":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

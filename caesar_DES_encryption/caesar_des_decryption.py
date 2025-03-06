import random
import string

# caesar_des_encryption.py
class CaesarDESCipher:
    def __init__(self, key: str, shift: int):
        self.key = key
        self.shift = shift % 26

    def encrypt(self, plaintext: str) -> str:
        return self._apply_caesar_cipher(plaintext, self.shift)

    def decrypt(self, ciphertext: str) -> str:
        return self._apply_caesar_cipher(ciphertext, -self.shift)

    def _apply_caesar_cipher(self, text: str, shift: int) -> str:
        return ''.join(self._shift_character(char, shift) for char in text)

    def _shift_character(self, char: str, shift: int) -> str:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + shift) % 26 + base)
        return char

    @staticmethod
    def generate_key() -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

if __name__ == "__main__":
    shift_value = int(input("Enter shift value: "))
    key = CaesarDESCipher.generate_key()
    cipher = CaesarDESCipher(key, shift_value)
    
    plaintext = input("Enter text to encrypt: ")
    encrypted_text = cipher.encrypt(plaintext)
    print(f"Encrypted Text: {encrypted_text}")
    print(f"Generated Key: {key}")
    
    decrypted_text = cipher.decrypt(encrypted_text)
    print(f"Decrypted Text: {decrypted_text}")

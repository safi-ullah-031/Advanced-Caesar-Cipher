# caesar_des_decryption.py
import random
import string

class CaesarDESCipher:
    def __init__(self, shift: int):
        self.key = self._generate_key()
        self.shift = shift % 26

    def decrypt(self, ciphertext: str) -> str:
        return self._apply_caesar_cipher(ciphertext, -self.shift)

    def _apply_caesar_cipher(self, text: str, shift: int) -> str:
        return ''.join(self._shift_character(char, shift) for char in text)

    def _shift_character(self, char: str, shift: int) -> str:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + shift) % 26 + base)
        return char

    def _generate_key(self) -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

if __name__ == "__main__":
    shift_value = int(input("Enter shift value: "))
    cipher = CaesarDESCipher(shift_value)
    
    print(f"Generated Key: {cipher.key}")
    ciphertext = input("Enter text to decrypt: ")
    decrypted_text = cipher.decrypt(ciphertext)
    print(f"Decrypted Text: {decrypted_text}")

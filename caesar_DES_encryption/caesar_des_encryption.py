# caesar_des_encryption.py
class CaesarDESCipher:
    def __init__(self, key: str, shift: int):
        self.key = key[:8]  # Take only the first 8 characters
        self.shift = shift % 26
        self.additional_shift = sum(ord(c) for c in self.key) % 26  # Second round shift

    def encrypt(self, plaintext: str) -> str:
        first_round = self._apply_caesar_cipher(plaintext, self.shift)
        second_round = self._apply_caesar_cipher(first_round, self.additional_shift)
        return second_round

    def _apply_caesar_cipher(self, text: str, shift: int) -> str:
        return ''.join(self._shift_character(char, shift) for char in text)

    def _shift_character(self, char: str, shift: int) -> str:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + shift) % 26 + base)
        return char

if __name__ == "__main__":
    key = input("Enter key (8 characters max): ")[:8]  # Ensure only first 8 characters are taken
    shift_value = int(input("Enter shift value: "))
    cipher = CaesarDESCipher(key, shift_value)
    
    plaintext = input("Enter text to encrypt: ")
    encrypted_text = cipher.encrypt(plaintext)
    print(f"Encrypted Text: {encrypted_text}")
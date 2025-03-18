# caesar_des_decryption.py
class CaesarDESCipher:
    def __init__(self, key: str, shift: int, rounds: int = 16):
        self.key = key[:8].ljust(8, ' ')  # Ensure key is exactly 8 characters
        self.shift = shift % 26
        self.rounds = rounds  # Total rounds of decryption
    def decrypt(self, ciphertext: str) -> str:
        text = ciphertext
        for _ in range(self.rounds):
            text = self._apply_caesar_cipher(text, -self.shift)
        return text
    def _apply_caesar_cipher(self, text: str, shift: int) -> str:
        return ''.join(self._shift_character(char, shift) for char in text)
    @staticmethod
    def _shift_character(char: str, shift: int) -> str:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + shift) % 26 + base)
        return char
if __name__ == "__main__":
    key = input("Enter 8-character key: ")
    shift_value = int(input("Enter shift value: "))
    ciphertext = input("Enter text to decrypt: ")
    
    cipher = CaesarDESCipher(key, shift_value)
    decrypted_text = cipher.decrypt(ciphertext)
    print(f"Decrypted Text: {decrypted_text}")
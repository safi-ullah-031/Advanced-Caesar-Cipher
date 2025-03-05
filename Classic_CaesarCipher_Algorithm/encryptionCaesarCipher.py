# encryptionCaesarCipher.py
class CaesarCipher:
    def __init__(self, shift: int):
        self.shift = shift % 26

    def encrypt(self, text: str) -> str:
        return ''.join(self._shift_character(char, self.shift) for char in text)

    def _shift_character(self, char: str, shift: int) -> str:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + shift) % 26 + base)
        return char

if __name__ == "__main__":
    shift_value = int(input("Enter shift value: "))
    cipher = CaesarCipher(shift_value)
    text = input("Enter the text to encrypt" + "(Do not use spaces): ")
    print(f"Encrypted Text: {cipher.encrypt(text)}")

# caesar_des_decryption.py
class CaesarDESCipher:
    def __init__(self, key: str, shift: int):
        self.key = key[:8]  # Take only the first 8 characters
        self.shift = shift % 26
        self.additional_shift = sum(ord(c) for c in self.key) % 26  # Second round shift
        self.third_shift = (self.shift + self.additional_shift) % 26  # Third round shift
        self.fourth_shift = (self.third_shift + self.additional_shift) % 26  # Fourth round shift
        self.fifth_shift = (self.fourth_shift + self.additional_shift) % 26  # Fifth round shift
        self.sixth_shift = (self.fifth_shift + self.additional_shift) % 26  # Sixth round shift

    def decrypt(self, ciphertext: str) -> str:
        first_round = self._apply_caesar_cipher(ciphertext, -self.sixth_shift)
        second_round = self._apply_caesar_cipher(first_round, -self.fifth_shift)
        third_round = self._apply_caesar_cipher(second_round, -self.fourth_shift)
        fourth_round = self._apply_caesar_cipher(third_round, -self.third_shift)
        fifth_round = self._apply_caesar_cipher(fourth_round, -self.additional_shift)
        sixth_round = self._apply_caesar_cipher(fifth_round, -self.shift)
        return sixth_round

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
    
    ciphertext = input("Enter text to decrypt: ")
    decrypted_text = cipher.decrypt(ciphertext)
    print(f"Decrypted Text: {decrypted_text}")
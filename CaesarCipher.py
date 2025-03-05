class CaesarCipher:
    def __init__(self, shift: int):
        self.shift = shift % 26  # Ensure shift stays within alphabet range

    def encrypt(self, text: str) -> str:
        return ''.join(self._shift_character(char, self.shift) for char in text)

    def decrypt(self, text: str) -> str:
        return ''.join(self._shift_character(char, -self.shift) for char in text)

    def _shift_character(self, char: str, shift: int) -> str:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + shift) % 26 + base)
        return char  # Non-alphabet characters remain unchanged

# Example Usage
if __name__ == "__main__":
    shift_value = 3  # Shift of 3 (Classic Caesar Cipher)
    cipher = CaesarCipher(shift_value)
    
    plaintext = "Safi Ullah"
    encrypted_text = cipher.encrypt(plaintext)
    decrypted_text = cipher.decrypt(encrypted_text)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted_text}")
    print(f"Decrypted: {decrypted_text}")

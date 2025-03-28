from caesar_des_base import CaesarDESBase

class CaesarDESCipherDecrypt(CaesarDESBase):
    def decrypt(self, ciphertext: str) -> str:
        text = ciphertext
        for _ in range(self.rounds):
            text = self._apply_caesar_cipher(text, -self.shift)  # Reverse shift
        return text

if __name__ == "__main__":
    key = input("Enter 8-character key: ")
    shift_value = int(input("Enter shift value: "))
    cipher = CaesarDESCipherDecrypt(key, shift_value)

    ciphertext = input("Enter text to decrypt: ")
    decrypted_text = cipher.decrypt(ciphertext)
    print(f"Decrypted Text: {decrypted_text}")

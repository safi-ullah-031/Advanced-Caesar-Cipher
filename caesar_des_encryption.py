from caesar_des_base import CaesarDESBase

class CaesarDESCipherEncrypt(CaesarDESBase):
    def encrypt(self, plaintext: str) -> str:
        text = plaintext
        for _ in range(self.rounds):
            text = self._apply_caesar_cipher(text, self.shift)
        return text

if __name__ == "__main__":
    key = input("Enter 8-character key: ")
    shift_value = int(input("Enter shift value: "))
    cipher = CaesarDESCipherEncrypt(key, shift_value)

    plaintext = input("Enter text to encrypt: ")
    encrypted_text = cipher.encrypt(plaintext)
    print(f"Encrypted Text: {encrypted_text}")

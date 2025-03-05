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

if __name__ == "__main__":
    shift_value = int(input("Enter shift value: "))  # User input for shift value
    cipher = CaesarCipher(shift_value)
    
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    text = input("Enter the text: ")
    
    if choice == 'e':
        print(f"Encrypted Text: {cipher.encrypt(text)}")
    elif choice == 'd':
        print(f"Decrypted Text: {cipher.decrypt(text)}")
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
